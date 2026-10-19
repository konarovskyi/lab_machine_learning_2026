# Setup troubleshooting

[Back to the setup guide](README.md)

| Symptom | What to do |
| --- | --- |
| A released lab cannot import its helper | Lab 1 and the setup notebook need no helper files. For later labs, keep all companion files together in your working copy; in Colab, upload `.py` companions into the active runtime. |
| `ModuleNotFoundError: numpy`, `matplotlib`, or `torch` | PyTorch is required. Locally, use the CPU PyTorch command in the [local guide](local.md), then install `setup/requirements.txt` with the same Python that launches JupyterLab. On MIN, use its Python 3 kernel and report missing packages to the teaching team. In Colab, follow its guide. In Nix, pull the updated flake and launch from `nix develop`. Restart the kernel after changing packages. |
| Imports work in a terminal but fail in the notebook | The kernel may use another Python. Check `sys.executable` in the setup notebook. Stop the old Jupyter server, launch from the intended environment, and choose its Python kernel. |
| `python3` or `py` is not found | Install Python or use the alternate command in the local guide, then reopen the terminal. You can also use MIN JupyterHub. |
| `venv` / `ensurepip` is missing on Linux | Your distribution may package venv separately. Follow its Python installation guidance or use MIN JupyterHub for the first class. Avoid installing course packages into the system Python. |
| PowerShell refuses an activation script | Use the direct `.\.venv\Scripts\python.exe` commands in the Windows guide; activation is not needed. |
| Nix reports an unsupported system | The supplied flake targets x86_64 Linux only. Choose local Python, MIN, or Colab on another system. |
| `CUDA available: False` | This is fine for Lab 1. Only CUDA is optional; the CPU PyTorch checks must pass. For later CUDA work, check a suitable MIN or Colab session. |
| Nix starts building CUDA or MAGMA | Pull the current course files and run `nix develop` from the course folder. The supplied flake has a single CPU environment with CUDA and ROCm explicitly disabled. Use MIN or Colab for optional GPU work. |
| A CPU-only Nix build takes too long | A binary substitute may be unavailable. Use MIN JupyterHub for class, or the local CPU-wheel route on a compatible non-NixOS system. Do not update the course lock file to work around this. |
| PyTorch has no compatible wheel | Check the Python version and system architecture against the official installation selector. Use MIN or Colab for the class instead of compiling PyTorch. |
| `NotImplementedError` in a released lab | This may mark an exercise to complete. Read the surrounding instructions. The separate setup notebook should complete without this error. |
| A variable is undefined or output seems stale | Run cells in order. After changing a definition, rerun it and the later cells that use it. Lab 1 has short blanks marked `...` or `TODO`; complete these before running the dependent examples and plots. Restart and run all after completing the notebook. |
| Lab 1 gives a shape error or an unexpectedly large loss | Inspect `.shape` on the input, target, and predictions. Lab 1 uses shape `(n, 1)` for all three. Follow the supplied reshape example and rerun affected cells. |
| Colab loses a released lab's helper after a new session starts | Re-upload it. Notebook storage and runtime storage are different. |
| Git reports modified files or refuses an update | Follow the [Git guide](git.md). Keep your work in `my-work`, preserve any edited originals, and ask for help rather than forcing an update. |

If you ask for help, include your operating system, chosen route, Python
version, first failing cell, and the complete error text. Include enough of
the message to identify the problem, but do not send passwords or login tokens.

Save your work before restarting a kernel or session. Keep a downloaded copy
of completed notebooks when using a hosted service.
