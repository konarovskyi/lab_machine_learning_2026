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

If access fails, check your UHH login and tell the teaching team. If a course
package is missing, send the error to the team so it can be coordinated with
MIN support. Do not replace the managed environment with a blanket package
upgrade as part of this setup.

Official references (checked 16 October 2026):

- [UHH login instructions](https://support.min.uni-hamburg.de/help/en-us/22-authentication/77-logging-in-to-jupyter-using-uhh-login)
- [Installed software; versions can change](https://support.min.uni-hamburg.de/help/en-us/26-software-and-libraries/91-important-software-packages-in-jupyter)
- [Shared resources and session limits](https://support.min.uni-hamburg.de/help/en-us/27-system/28-limitations-in-jupyter)
- [Installing additional packages](https://support.min.uni-hamburg.de/help/en-us/26-software-and-libraries/90-installing-software-packages-in-jupyter)
