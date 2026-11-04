"""Supplied infrastructure for Lab 2: handwritten-digit recognition.

Read the notebooks for the exercises. Students may inspect this file, but do
not need to reproduce its data loading, plotting, or training loop. The loop
will be studied in Lab 3. Images use (batch, channels, height, width); network
outputs are raw class scores, not softmax probabilities.
"""

from pathlib import Path
import math

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageOps
import torch
from torch import nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms


def make_loaders(root="data", batch_size=128, train_size=10000,
                 val_size=2000, seed=2026, download=True):
    """Return train, validation, test loaders for a small MNIST experiment.

    Training and validation use disjoint, seeded subsets of the official
    60,000 training examples; unused training examples stay unused. The final
    test loader contains all 10,000 official test examples. Keep it untouched
    until architecture choices have been made using validation data.

    ToTensor maps grayscale pixels to float32 values in [0, 1] with shape
    (1, 28, 28). The loader adds a batch dimension. Labels are int64 integers.
    num_workers=0 also works in hosted notebooks and on Windows.
    """
    if train_size <= 0 or val_size <= 0 or batch_size <= 0:
        raise ValueError("Training size, validation size and batch size must be positive.")
    transform = transforms.ToTensor()
    training_data = datasets.MNIST(root, train=True, download=download,
                                   transform=transform)
    if train_size + val_size > len(training_data):
        raise ValueError("Training and validation sizes exceed the available training data.")
    test_data = datasets.MNIST(root, train=False, download=download,
                              transform=transform)
    split_generator = torch.Generator().manual_seed(seed)
    indices = torch.randperm(len(training_data), generator=split_generator).tolist()
    train_data = Subset(training_data, indices[:train_size])
    val_data = Subset(training_data, indices[train_size:train_size + val_size])
    shuffle_generator = torch.Generator().manual_seed(seed)
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True,
                              generator=shuffle_generator, num_workers=0)
    val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False,
                            num_workers=0)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False,
                             num_workers=0)
    return train_loader, val_loader, test_loader


def _evaluate(model, loader, criterion, device):
    """Sample-weighted loss and accuracy; criterion must return a mean loss."""
    model.eval()
    total_loss, correct, total = 0.0, 0, 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            scores = model(images)
            loss = criterion(scores, labels)
            total_loss += loss.item() * len(labels)
            correct += (scores.argmax(dim=1) == labels).sum().item()
            total += len(labels)
    if total == 0:
        raise ValueError("Cannot evaluate an empty dataset.")
    return {"loss": total_loss / total, "accuracy": correct / total}


def train_model(model, train_loader, val_loader, *, criterion, device,
                epochs=3, learning_rate=0.001, seed=2026):
    """Train in place with Adam and return one dictionary per epoch.

    criterion should be nn.CrossEntropyLoss() with its default mean reduction.
    History keys: epoch, train_loss, val_loss, val_accuracy. Training loss is
    averaged over the batches while the model changes; validation loss is
    evaluated with the final parameters of each epoch. These are different
    measurements, so training loss need not be below validation loss.

    Each call creates a fresh optimizer and restarts the batch-shuffle seed.
    For a fresh experiment, construct a NEW model after torch.manual_seed(seed).
    This function does not reset model parameters. Seeds make comparisons
    easier to reproduce but do not guarantee identical CPU/GPU results.
    """
    if epochs <= 0 or learning_rate <= 0:
        raise ValueError("Epochs and learning rate must be positive.")
    if getattr(criterion, "reduction", "mean") != "mean":
        raise ValueError("Use a loss with mean reduction for this supplied trainer.")
    torch.manual_seed(seed)
    if train_loader.generator is not None:
        train_loader.generator.manual_seed(seed)
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    history = []
    for epoch in range(1, epochs + 1):
        model.train()
        total_loss, total = 0.0, 0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            scores = model(images)
            loss = criterion(scores, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(labels)
            total += len(labels)
        if total == 0:
            raise ValueError("Cannot train on an empty dataset.")
        validation = _evaluate(model, val_loader, criterion, device)
        row = {"epoch": epoch, "train_loss": total_loss / total,
               "val_loss": validation["loss"],
               "val_accuracy": validation["accuracy"]}
        history.append(row)
        print(f"Epoch {epoch}/{epochs}: train loss {row['train_loss']:.4f}; "
              f"validation loss {row['val_loss']:.4f}; "
              f"validation accuracy {row['val_accuracy']:.1%}")
    return history


def evaluate_model(model, loader, device):
    """Return {'loss': mean cross-entropy, 'accuracy': fraction correct}.

    Expects raw class scores and integer labels. Leaves the model in evaluation
    mode. The test loader should be used only for final evaluation.
    """
    model.to(device)
    return _evaluate(model, loader, nn.CrossEntropyLoss(), device)


def predict_images(model, images, device):
    """Return CPU class scores for images with shape (batch, 1, 28, 28).

    Process at most 128 images at once, so inspecting the entire validation
    set does not require keeping all its feature maps in GPU memory.
    """
    if images.ndim != 4 or tuple(images.shape[1:]) != (1, 28, 28):
        raise ValueError("Expected image shape (batch, 1, 28, 28).")
    if len(images) == 0:
        raise ValueError("Provide at least one image to predict.")
    model.to(device)
    model.eval()
    with torch.no_grad():
        scores = [model(batch.to(device)).detach().cpu()
                  for batch in images.split(128)]
    return torch.cat(scores)


def count_parameters(model):
    """Count trainable scalar parameters, including biases."""
    return sum(parameter.numel() for parameter in model.parameters()
               if parameter.requires_grad)


def show_images(images, labels=None, predictions=None, max_images=12):
    """Display a small image grid; labels/predictions are optional. Return None."""
    images = images.detach().cpu()
    if images.ndim == 3:
        images = images.unsqueeze(0)
    n = min(len(images), max_images)
    if n <= 0:
        print("No images to display.")
        return
    columns = min(6, n)
    rows = math.ceil(n / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(2 * columns, 2.4 * rows),
                              squeeze=False)
    for index, ax in enumerate(axes.flat):
        ax.axis("off")
        if index < n:
            ax.imshow(images[index, 0], cmap="gray", vmin=0, vmax=1)
            title = []
            if labels is not None:
                title.append(f"Label: {int(labels[index])}")
            if predictions is not None:
                title.append(f"Prediction: {int(predictions[index])}")
            ax.set_title("\n".join(title))
    fig.tight_layout()
    plt.show()
    plt.close(fig)


def plot_history(history):
    """Plot loss and validation accuracy; return None."""
    epochs = [row["epoch"] for row in history]
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
    axes[0].plot(epochs, [row["train_loss"] for row in history], "o-", label="Training")
    axes[0].plot(epochs, [row["val_loss"] for row in history], "o-", label="Validation")
    axes[0].set(xlabel="Epoch", ylabel="Cross-entropy loss")
    axes[0].legend()
    axes[1].plot(epochs, [row["val_accuracy"] for row in history], "o-")
    axes[1].set(xlabel="Epoch", ylabel="Validation accuracy", ylim=(0, 1))
    for ax in axes:
        ax.set_xticks(epochs)
        ax.grid(alpha=0.25)
    fig.tight_layout()
    plt.show()
    plt.close(fig)


def _prepare_digit(image, invert):
    image = ImageOps.exif_transpose(image).convert("L")
    low, high = image.getextrema()
    if high - low < 20:
        raise ValueError("The image is blank or has little contrast; use a clear single digit.")
    if invert:
        image = ImageOps.invert(image)
    image = ImageOps.autocontrast(image)
    # Threshold only to find a bounding box; retain grayscale values afterwards.
    foreground = image.point(lambda value: 255 if value >= 64 else 0)
    box = foreground.getbbox()
    if box is None:
        raise ValueError("No digit found; check foreground/background and invert.")
    digit = image.crop(box)
    scale = 20 / max(digit.size)
    size = (max(1, round(digit.width * scale)), max(1, round(digit.height * scale)))
    digit = digit.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("L", (28, 28), color=0)
    canvas.paste(digit, ((28 - digit.width) // 2, (28 - digit.height) // 2))
    return transforms.ToTensor()(canvas)


def load_digit(path, invert=True):
    """Read a single digit and return a CPU float tensor of shape (1, 28, 28).

    Use a tightly framed image of one dark digit on a plain light background
    (invert=True), or a light digit on a dark background (invert=False). EXIF
    orientation is applied; grayscale foreground is cropped, fitted within a
    20-by-20 box preserving aspect ratio, and centred on a black 28-by-28 image.
    Values lie in [0, 1]. Inspect the result before predicting. This simple
    preparation cannot reliably remove shadows or handle complicated photos.
    """
    with Image.open(Path(path)) as image:
        return _prepare_digit(image, invert)


def make_example_digits():
    """Return three deterministic drawn examples (0, 1, 7), shape (3, 1, 28, 28).

    These are illustrative drawings generated here, not samples from MNIST.
    Correct predictions are not guaranteed: compare their appearance with the
    training images. No additional image files or download is needed.
    """
    drawings = []
    for digit in (0, 1, 7):
        canvas = Image.new("L", (112, 112), color=255)
        draw = ImageDraw.Draw(canvas)
        if digit == 0:
            draw.ellipse((28, 16, 82, 98), outline=0, width=10)
        elif digit == 1:
            draw.line([(37, 35), (57, 17), (57, 97)], fill=0, width=10)
        else:
            draw.line([(25, 20), (85, 20), (43, 97)], fill=0, width=10)
        drawings.append(_prepare_digit(canvas, invert=True))
    return torch.stack(drawings)


# Supplied optional interface. The frontend runs inside the notebook's widget
# manager; the trained PyTorch model and inference stay in its Python kernel.
_DIGIT_DRAWER_ESM = r"""
function render({ model, el }) {
  const root = document.createElement('div');
  root.style.cssText = 'font:15px system-ui,sans-serif;color:#183e5a;max-width:650px;padding:16px;border:1px solid #cbd5e1;border-radius:10px;background:#f8fafc';
  root.innerHTML = `
    <p style="margin:0 0 12px">Write one digit (0–9) with your mouse, pen, or finger.</p>
    <div style="display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start">
      <canvas width="280" height="280" aria-label="Draw a handwritten digit"
        style="width:280px;max-width:100%;height:auto;border:1px solid #64748b;border-radius:4px;touch-action:none;cursor:crosshair;background:white"></canvas>
      <div style="max-width:270px">
        <p style="margin-top:0">Image seen by your network (28 × 28)</p>
        <img alt="Prepared digit" width="112" height="112" hidden
          style="image-rendering:pixelated;border:1px solid #94a3b8">
        <p class="prediction" style="font-size:24px;font-weight:600;min-height:30px"></p>
        <p class="probability"></p>
      </div>
    </div>
    <div style="display:flex;gap:10px;margin-top:12px">
      <button type="button" class="recognise" disabled
        style="background:#183e5a;color:white;border:0;border-radius:5px;padding:9px 18px;cursor:pointer">Recognise</button>
      <button type="button" class="clear"
        style="background:white;color:#183e5a;border:1px solid #64748b;border-radius:5px;padding:9px 18px;cursor:pointer">Clear</button>
    </div>
    <p class="status" role="status" aria-live="polite" style="margin-bottom:0">Draw a digit, then click Recognise.</p>`;
  el.appendChild(root);
  const canvas = root.querySelector('canvas');
  const ctx = canvas.getContext('2d');
  const preview = root.querySelector('img');
  const prediction = root.querySelector('.prediction');
  const probability = root.querySelector('.probability');
  const status = root.querySelector('.status');
  const recognise = root.querySelector('.recognise');
  const clear = root.querySelector('.clear');
  let sequence = Number((model.get('request') || {}).id || 0);
  let current = sequence;
  let activePointer = null;
  let hasInk = false;
  let busy = false;
  let timer;

  function whiteCanvas() {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = '#111111';
    ctx.fillStyle = '#111111';
    ctx.lineWidth = 22;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
  }
  function buttons() { recognise.disabled = busy || !hasInk; }
  function invalidate(message) {
    current = ++sequence;
    clearTimeout(timer);
    busy = false;
    preview.hidden = true;
    preview.removeAttribute('src');
    prediction.textContent = '';
    probability.textContent = '';
    status.textContent = message;
    // Also discard the Python-side saved result when the drawing changes.
    model.set('request', {id: current, png: ''});
    model.save_changes();
    buttons();
  }
  function point(event) {
    const rect = canvas.getBoundingClientRect();
    return [(event.clientX - rect.left) * canvas.width / rect.width,
            (event.clientY - rect.top) * canvas.height / rect.height];
  }
  function down(event) {
    if (activePointer !== null || (event.pointerType === 'mouse' && event.button !== 0)) return;
    event.preventDefault();
    activePointer = event.pointerId;
    canvas.setPointerCapture(event.pointerId);
    hasInk = true;
    invalidate('Ready. Click Recognise when your digit is complete.');
    const [x, y] = point(event);
    ctx.beginPath();
    ctx.arc(x, y, ctx.lineWidth / 2, 0, 2 * Math.PI);
    ctx.fill();
    ctx.beginPath();
    ctx.moveTo(x, y);
  }
  function move(event) {
    if (event.pointerId !== activePointer) return;
    event.preventDefault();
    const [x, y] = point(event);
    ctx.lineTo(x, y);
    ctx.stroke();
  }
  function up(event) {
    if (event.pointerId !== activePointer) return;
    activePointer = null;
    ctx.closePath();
    if (canvas.hasPointerCapture(event.pointerId)) canvas.releasePointerCapture(event.pointerId);
  }
  function reset() {
    activePointer = null;
    hasInk = false;
    whiteCanvas();
    invalidate('Draw a digit, then click Recognise.');
  }
  function submit() {
    if (!hasInk || busy) return;
    current = ++sequence;
    busy = true;
    status.textContent = 'Your trained network is reading the digit…';
    buttons();
    model.set('request', {id: current, png: canvas.toDataURL('image/png')});
    model.save_changes();
    timer = setTimeout(() => {
      busy = false;
      buttons();
      status.textContent = 'No reply yet. Check that the Python kernel is running, then try Recognise again.';
    }, 15000);
  }
  function receive() {
    const result = model.get('response') || {};
    if (result.id !== current) return; // Ignore a reply for an erased/changed digit.
    clearTimeout(timer);
    busy = false;
    buttons();
    if (result.error) {
      preview.hidden = true;
      prediction.textContent = '';
      probability.textContent = '';
      status.textContent = result.error;
    } else if (result.preview) {
      preview.src = result.preview;
      preview.hidden = false;
      prediction.textContent = `Predicted digit: ${result.label}`;
      probability.textContent = `Model probability: ${(100 * result.probability).toFixed(1)}%`;
      status.textContent = 'Compare the result with what you wrote. Use Clear to try another digit.';
    }
  }

  whiteCanvas();
  const saved = model.get('request') || {};
  let disposed = false;
  if (saved.png) {
    const image = new Image();
    const savedId = current;
    image.onload = () => {
      if (disposed || savedId !== current) return;
      ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
      hasInk = true;
      buttons();
    };
    image.src = saved.png;
  }
  const handlers = [['pointerdown', down], ['pointermove', move],
                    ['pointerup', up], ['pointercancel', up], ['lostpointercapture', up]];
  handlers.forEach(([event, handler]) => canvas.addEventListener(event, handler));
  recognise.addEventListener('click', submit);
  clear.addEventListener('click', reset);
  model.on('change:response', receive);
  receive();
  return () => {
    disposed = true;
    clearTimeout(timer);
    handlers.forEach(([event, handler]) => canvas.removeEventListener(event, handler));
    recognise.removeEventListener('click', submit);
    clear.removeEventListener('click', reset);
    model.off('change:response', receive);
    root.remove();
  };
}
export default { render };
"""


def digit_drawer(model, device):
    """Return an optional notebook canvas connected to an already trained model.

    Requires anywidget (only imported here), a running Python kernel, and a
    compatible Jupyter widget frontend. In Colab enable its custom widget manager
    first. Draw with a mouse/pen/touch, then click Recognise. The same image
    preparation as load_digit is applied before inference. Nothing is retrained.

    After a successful prediction, last_image is the prepared CPU tensor
    (1, 28, 28) and last_prediction is its predicted integer label. Use these
    in an ordinary plotting cell to preserve the result in a saved notebook.
    Clear or changing the drawing invalidates that saved result. Close the old
    widget before creating another one after retraining the network.
    """
    import base64
    import io

    try:
        import anywidget
        import traitlets
    except ImportError as error:
        raise ImportError(
            "The optional drawing pad needs anywidget. See the drawing-cell "
            "instructions or use the existing PNG/JPEG image option."
        ) from error

    class DigitDrawer(anywidget.AnyWidget):
        _esm = _DIGIT_DRAWER_ESM
        request = traitlets.Dict().tag(sync=True)
        response = traitlets.Dict().tag(sync=True)

        def __init__(self):
            self.last_image = None
            self.last_prediction = None
            super().__init__()

        @traitlets.observe("request")
        def _recognise(self, change):
            request = change["new"]
            request_id = request.get("id", 0)
            png = request.get("png", "")
            self.last_image = None
            self.last_prediction = None
            if not png:
                self.response = {"id": request_id}
                return
            try:
                prefix = "data:image/png;base64,"
                if not isinstance(png, str) or not png.startswith(prefix) or len(png) > 1000000:
                    raise ValueError("Please draw one digit in the canvas and try again.")
                raw = base64.b64decode(png[len(prefix):], validate=True)
                with Image.open(io.BytesIO(raw)) as image:
                    if image.size != (280, 280):
                        raise ValueError("The drawing should come from the 280-by-280 canvas.")
                    prepared = _prepare_digit(image, invert=True)
                scores = predict_images(model, prepared.unsqueeze(0), device)[0]
                if tuple(scores.shape) != (10,) or not torch.isfinite(scores).all():
                    raise ValueError("The model must return ten finite class scores per image.")
                label = int(scores.argmax())
                probabilities = scores.softmax(dim=0)
                buffer = io.BytesIO()
                transforms.ToPILImage()(prepared).save(buffer, format="PNG")
                self.last_image = prepared.clone()
                self.last_prediction = label
                self.response = {
                    "id": request_id, "label": label,
                    "probability": float(probabilities[label]),
                    "preview": prefix + base64.b64encode(buffer.getvalue()).decode("ascii"),
                }
            except Exception as error:
                # Widget callbacks otherwise hide exceptions in some frontends.
                self.response = {"id": request_id, "error": str(error)}

    return DigitDrawer()
