# Set up before the first lab

**Contemporary Machine Learning in Theory and Practice, WS26/27**  
First lab: **Thursday, 22 October 2026, 16:15-17:45**.

Choose **one** of the following routes. You may use any of them throughout the
course. If you already have a working environment, keep it and run the checks.

| Route | When to choose it | Instructions |
| --- | --- | --- |
| 1. Local Python/Jupyter | You want to compute on your own laptop, including offline after installation. | [Windows, macOS, Linux](local.md) |
| 2. MIN JupyterHub | Recommended if you do not have a working local environment. Also recommended for access to university CUDA resources in later labs. | [UHH login and files](jupyterhub.md) |
| 3. Google Colab | You prefer another browser-based environment and have a Google account. | [Upload and save notebooks](colab.md) |
| 4. Nix | You already use Nix on an x86_64 Linux machine. | [Use the supplied flake](nix.md) |

**For Lab 1:** Python 3.10 or later, NumPy, Matplotlib, and a Python notebook
interface. A normal CPU is sufficient. You do not need to install PyTorch,
CUDA, a GPU driver, or LaTeX before this class. Later lab instructions will
announce additional packages when needed. Hosted services may use different
package versions; the required checks are the same.

## 1. Get the files

Open the **student repository** using the link supplied on Moodle. The short
[Git guide](git.md) explains how to clone it and get updates. Its root is the
**course folder** referred to in these instructions. Initially it contains
only setup materials. Lab folders will be added shortly before each class.

For MIN JupyterHub or Colab, you may instead download the setup notebook
from that repository and upload it as described in your route.
You do not need a local Git installation for that workflow.

Keep your notebook copies in `my-work`, which Git ignores, as explained in
the Git guide. This separates your work from the supplied files when updating.

| File | What it is for |
| --- | --- |
| `setup/check_setup.ipynb` | A short check with no exercises to solve. |
| `setup/requirements.txt` | The packages needed to complete the setup. |
| `setup/git.md` | Getting the materials, receiving updates, and keeping your work. |
| `flake.nix`, `flake.lock` | The course environment for the Nix route. |

Keep this folder structure for local Python, MIN JupyterHub, and Nix.
The setup notebook is self-contained. No lab notebook or helper is needed yet.

## 2. Open and check your environment

Follow your route above. In a Git checkout, copy `setup/check_setup.ipynb` into
`my-work/check_setup.ipynb` and open that copy; create `my-work` first if needed.
Select a Python kernel if prompted and run its cells using **Shift+Enter**.
The notebook checks Python, NumPy, a matrix calculation, and a plot.
It installs nothing and does not contain lab exercises.

You are ready when:

- the required cells complete without an error and print the success message;
- you can see the plotted curve;
- you can save your notebook copy and reopen it.

The final PyTorch/CUDA section is **optional**. A message saying that PyTorch
is absent or CUDA is unavailable does not prevent you from doing Lab 1.

## 3. Know how to use a notebook

An `.ipynb` file contains text cells, Python code cells, and saved output.
The **kernel** is the Python process that runs the code and remembers variables.
Run cells in order. After changing a definition, rerun it and the cells that
depend on it. Restarting the kernel clears variables, not the saved notebook.

In JupyterLab, use **Kernel > Restart Kernel and Run All Cells** to check a
completed notebook from a clean state. In Colab, restart the session and run
all cells from the Runtime menu. Save with Ctrl+S (Cmd+S on macOS). For a
submission, retain the `.ipynb` file with your work and outputs, not a screenshot
or the browser's HTML page.

Before each class, obtain the latest materials as described in the Git guide.
The corresponding lab folder will contain its exercise notebook and any
companion files. Follow that lab's instructions when it is released.

## If something fails

See [troubleshooting](troubleshooting.md). Note your route, the first failing
cell, and its full error message so that we can help at the lab. If a local
installation becomes difficult, use MIN JupyterHub for the first class.

Bring your laptop and charger. For a hosted route, check beforehand that you
can sign in and use the university network from that laptop.
