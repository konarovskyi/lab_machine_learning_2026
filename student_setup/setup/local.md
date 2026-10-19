# Route 1: Local Python and JupyterLab

[Back to the setup guide](README.md)

Use Python 3.10 or later with a compatible PyTorch 2 installation. For a new
setup, Python 3.12 is a suitable choice. If Python is missing, install it from
[python.org](https://www.python.org/downloads/), then reopen your terminal.
Keep an already working notebook environment if it passes the setup check.

Open a terminal in the **course folder**, the root of your student repository
copy. It contains `setup/`. These commands belong in the terminal. Create one
environment for all labs, and install CPU PyTorch before the other requirements.
This avoids downloading CUDA packages for the compulsory exercises.

## Linux (bash or zsh)

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "torch>=2.2,<3" --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r setup/requirements.txt
python -m jupyterlab
```

For NixOS, use the [Nix route](nix.md) instead of installing generic Linux wheels.

## macOS (bash or zsh)

The macOS wheel supports CPU computation. Use the standard package index:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "torch>=2.2,<3"
python -m pip install -r setup/requirements.txt
python -m jupyterlab
```

If your Python or Mac architecture has no compatible wheel, use MIN JupyterHub
or Colab for the class rather than compiling PyTorch.

On later days, on Linux or macOS, start from the same folder and run only:

```bash
source .venv/bin/activate
python -m jupyterlab
```

## Windows (PowerShell)

These commands use the environment's Python directly, so PowerShell script
activation is unnecessary:

```powershell
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install "torch>=2.2,<3" --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install -r setup\requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

If `py` is unavailable but `python --version` reports a suitable Python 3,
use `python -m venv .venv` for the creation step. On later days, run the last
command again from this folder. There is no need to change PowerShell's
execution policy.

## In the browser

Keep the launching terminal open. If the browser does not open automatically,
use the local URL printed by JupyterLab. Open a copy of
`setup/check_setup.ipynb` in `my-work` with a Python kernel and complete all
required cells, including the CPU PyTorch check. Create `my-work` in the
course folder using your file manager or JupyterLab's file browser.
No lab folder is needed for setup.

Save your work before stopping JupyterLab with Ctrl+C in its terminal.
Your notebooks belong outside `.venv`.

## Updating an existing course environment

If the earlier NumPy-only setup is already installed, reuse it. Activate it
(or use its Python executable on Windows), run the PyTorch installation
command above for your system, and install `setup/requirements.txt` again.
Restart JupyterLab and rerun the setup check. An existing compatible CUDA
build of PyTorch can also run all required exercises on the CPU and need
not be replaced.

For later labs, reuse this environment and install the requirements file
named in that lab's instructions.

Official references: [PyTorch installation selector](https://pytorch.org/get-started/locally/),
[Python virtual environments](https://docs.python.org/3/library/venv.html),
[Python on Windows](https://docs.python.org/3/using/windows.html),
[JupyterLab installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).
