# Route 2: MIN JupyterHub

[Back to the setup guide](README.md)

This is the recommended route if you do not have a working local environment.
It is also useful for CUDA work in later labs: calculations run on university
servers, so your laptop does not need an NVIDIA GPU.

1. Open [code.min.uni-hamburg.de](https://code.min.uni-hamburg.de).
2. Choose **UHH-Login** and sign in with your central university user ID and
   password. Start your session if prompted.
3. In the JupyterLab file browser, create a course folder and upload
   `check_setup.ipynb` there. Alternatively, clone the student repository
   in a JupyterLab terminal following the [Git guide](git.md), and copy
   `setup/check_setup.ipynb` into `my-work` before running it.
4. Open your setup notebook copy, choose the provided **Python 3** kernel,
   and run the required cells. Use the supplied server environment first.
5. Save the notebook on the server and download a copy to your laptop.
   No lab exercises or helper files are needed for this setup check.

On 16 October 2026 the instructor tested the previous NumPy lab here, and
a separate PyTorch test completed a CUDA matrix computation on a Quadro RTX
5000. These are observations from one session. For the revised PyTorch lab,
run the current required CPU checks in your own session before class.

The required notebook checks verify that PyTorch works on the CPU. The
final optional cell only reports GPU availability. A GPU is a shared resource,
so access is not a reservation. For Lab 1, use the CPU. Shut down GPU kernels when finished with
later GPU work to release resources.

If access fails, check your UHH login and tell the teaching team. For a missing
or incompatible Lab 2 package, try the
[targeted repair instructions](troubleshooting.md#lab-2-libraries-and-the-drawing-canvas)
first. They include the instructor's successful torchvision command for
PyTorch `2.12.0+cu130`, with a version check before installing.

For the optional drawing canvas, install `anywidget` in a notebook cell with
`%pip install "anywidget>=0.9.18,<1"`. If you see
`Failed to load model class 'AnyModel' from module 'anywidget'`, save all open
notebooks and use **File → Hub Control Panel → Stop My Server → Start My Server**.
Reopen JupyterLab and hard-refresh the browser. Rerun completed setup, model,
and training cells before trying the pad again. A kernel restart alone may
not load the browser extension. If the repair fails, send the full error to
the tutor and use Exercise 6's PNG/JPEG option or supplied examples.

Official references (checked 16 October 2026):

- [UHH login instructions](https://support.min.uni-hamburg.de/help/en-us/22-authentication/77-logging-in-to-jupyter-using-uhh-login)
- [Installed software; versions can change](https://support.min.uni-hamburg.de/help/en-us/26-software-and-libraries/91-important-software-packages-in-jupyter)
- [Shared resources and session limits](https://support.min.uni-hamburg.de/help/en-us/27-system/28-limitations-in-jupyter)
- [Installing additional packages](https://support.min.uni-hamburg.de/help/en-us/26-software-and-libraries/90-installing-software-packages-in-jupyter)


Lab 2 restart instructions checked 3 November 2026: [MIN server restart](https://support.min.uni-hamburg.de/help/en-us/27-system/30-jupyterlab-instanz-neu-starten).
