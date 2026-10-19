# Machine learning labs

**Contemporary Machine Learning in Theory and Practice, WS26/27**

Before the first lab on **22 October 2026**, follow the
[setup guide](setup/README.md) and run [check_setup.ipynb](setup/check_setup.ipynb).
Choose one of four routes: local Python/Jupyter, MIN JupyterHub, Google Colab,
or the supplied Nix environment. All routes use the same lab notebooks.

This repository starts with setup information. Each lab folder will be added
shortly before its class. You can complete all setup checks now, without any
lab exercises or helper files.

New to Git? Read the short [Git guide](setup/git.md) to obtain the files and
download updates before each class. Keep your own work in the ignored
`my-work` folder as explained there.

Lab 1 introduces **PyTorch on the CPU** through tensors, simple operations,
noisy regression data, and a small neural network. No previous PyTorch or
NumPy experience is assumed. Short examples and templates guide your code;
plotting and most of the training code are supplied. Jupyter provides the
notebook interface, and Matplotlib draws the plots. NumPy is installed as
part of the environment, but you will work with PyTorch tensors in Lab 1.

When Lab 1 is released, copy its folder to `my-work/lab_01` as shown in the
[Git guide](setup/git.md). Read `lab_01.pdf` and work in your copy of
`lab_01.ipynb`. The PDF and notebook use the same exercise numbers.
Work through the examples and tasks in order, predict what will
happen before running code, and write brief explanations alongside your
results. The notebook includes the tutorial exercises and homework and
needs no helper files. Save your completed `.ipynb` with its outputs.

Complete the setup checks before class. A GPU and CUDA are unnecessary for
Lab 1; the supplied Nix environment is CPU-only. Additional dependencies
will be announced with later labs.
