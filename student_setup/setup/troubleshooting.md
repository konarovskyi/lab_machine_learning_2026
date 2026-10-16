# Setup troubleshooting

[Back to the setup guide](README.md)

| Symptom | What to do |
| --- | --- |
| A released lab cannot import its helper | Keep all files from that lab together in your working copy. In Colab, upload the `.py` companion into the active runtime. The setup notebook itself needs no helper. |
| `ModuleNotFoundError: numpy` or `matplotlib` | Locally, install `setup/requirements.txt` using the same environment that launches JupyterLab. On MIN, use its Python 3 kernel and report missing packages to the teaching team. In Colab, follow the package cell in its guide. In Nix, launch JupyterLab from `nix develop`. |
| Imports work in a terminal but fail in the notebook | The kernel may use another Python. Check `sys.executable` in the setup notebook. Stop the old Jupyter server, launch from the intended environment, and choose its Python kernel. |
| `python3` or `py` is not found | Install Python or use the alternate command in the local guide, then reopen the terminal. You can also use MIN JupyterHub. |
| `venv` / `ensurepip` is missing on Linux | Your distribution may package venv separately. Follow its Python installation guidance or use MIN JupyterHub for the first class. Avoid installing course packages into the system Python. |
| PowerShell refuses an activation script | Use the direct `.\.venv\Scripts\python.exe` commands in the Windows guide; activation is not needed. |
| Nix reports an unsupported system | The supplied flake targets x86_64 Linux only. Choose local Python, MIN, or Colab on another system. |
| No PyTorch, or `CUDA available: False` | This is fine for Lab 1. Both are optional in the setup notebook. For later CUDA work, check a suitable MIN or Colab session. |
| `NotImplementedError` in a released lab | This may mark an exercise to complete. Read the surrounding instructions. The separate setup notebook should complete without this error. |
| A variable is undefined or output seems stale | Run cells in order. Restart the kernel/session and rerun the notebook. An unfinished Lab 1 still stops at its exercise cells. |
| Colab loses a released lab's helper after a new session starts | Re-upload it. Notebook storage and runtime storage are different. |
| Git reports modified files or refuses an update | Follow the [Git guide](git.md). Keep your work in `my-work`, preserve any edited originals, and ask for help rather than forcing an update. |

If you ask for help, include your operating system, chosen route, Python
version, first failing cell, and the complete error text. Include enough of
the message to identify the problem, but do not send passwords or login tokens.

Save your work before restarting a kernel or session. Keep a downloaded copy
of completed notebooks when using a hosted service.
