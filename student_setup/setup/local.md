# Route 1: Local Python and JupyterLab

[Back to the setup guide](README.md)

Use Python 3.10 or later. If Python is missing, install a supported Python 3
release from [python.org](https://www.python.org/downloads/), then reopen your
terminal. Keep an already working notebook environment if it passes the check.

Open a terminal in the **course folder**, the root of your student repository
copy. It contains the `setup` folder. The commands below belong in
the terminal, not in a notebook cell. Create one environment here for the labs.

## macOS and Linux (bash or zsh)

Check the version, create the environment, install the packages, and start
JupyterLab:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r setup/requirements.txt
python -m jupyterlab
```

On a later day, start from the same folder and run only:

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
.\.venv\Scripts\python.exe -m pip install -r setup\requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

If `py` is unavailable but `python --version` reports a suitable Python 3,
use `python -m venv .venv` for the creation step. On later days, run the last
command again from this folder. There is no need to change your system's
PowerShell execution policy.

## In the browser

Keep the launching terminal open. If the browser does not open automatically,
use the local URL printed by JupyterLab. In its file browser, open
a copy of `setup/check_setup.ipynb` in `my-work` with a Python kernel and
complete the required cells. Create `my-work` in the course folder using your
file manager or JupyterLab's file browser. No lab folder is needed for setup.

Save your work before stopping JupyterLab with Ctrl+C in its terminal.
Your notebooks belong in the course folder, outside `.venv`.

For later labs, activate/reuse this environment and install the requirements
file named in that lab's instructions. Do not install a semester-wide list
of machine-learning frameworks now.

Official references: [Python virtual environments](https://docs.python.org/3/library/venv.html),
[Python on Windows](https://docs.python.org/3/using/windows.html),
[JupyterLab installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).
