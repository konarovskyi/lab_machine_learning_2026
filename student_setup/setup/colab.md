# Route 3: Google Colab

[Back to the setup guide](README.md)

You need a Google account and a browser. Download the course files to your
laptop first. No local Git installation or Drive mount is needed.

1. Open [Google Colab](https://colab.research.google.com) and sign in.
2. Choose **File > Upload notebook** and select `setup/check_setup.ipynb`.
3. Connect to a Python runtime. Use the normal CPU runtime for Lab 1.
4. Run the required setup cells. This notebook is self-contained and needs
   no helper files or lab exercises.
5. Save a copy of your notebook in Drive or download it using **File > Download >
   Download .ipynb**. Reopen it to check that you can retain your work.

When Lab 1 is released, upload `lab_01.ipynb` in the same way and keep the
exercise PDF open alongside it. The notebook needs no helper files. Its
supplied plotting and training code is already in the notebook. Run cells
in order, complete the marked tasks, and save your own copy with outputs.

For later labs, upload any Python helper files separately using the runtime's
**Files** panel. Opening an `.ipynb` does not upload its companions. Uploaded
runtime files and Python variables are temporary. Saving the notebook in
Drive does not preserve those files, so re-upload companions after a new
runtime starts.

NumPy, Matplotlib, and PyTorch are normally available. Use the supplied
versions if the required checks pass. If NumPy or Matplotlib is missing or
outdated, run this in a notebook cell, restart the session, and rerun the checks:

```python
%pip install "numpy>=1.24" "matplotlib>=3.7"
```

If PyTorch is missing or older than version 2.2, the CPU installation is:

```python
%pip install "torch>=2.2,<3" --index-url https://download.pytorch.org/whl/cpu
```

Restart the session afterwards. Do not replace a working Colab PyTorch
installation merely because it also supports CUDA. Lab 1 explicitly uses CPU
tensors. It has no helper files to upload.

Colab already supplies the notebook interface; do not launch a JupyterLab
server inside it. For a later GPU lab, select **Runtime > Change runtime type**
and an available GPU. GPU availability varies.

Official references: [Colab FAQ](https://research.google.com/colaboratory/faq.html),
[file upload examples](https://colab.research.google.com/notebooks/io.ipynb).
