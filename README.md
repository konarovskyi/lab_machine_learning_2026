# Machine learning labs

**Contemporary Machine Learning in Theory and Practice, WS26/27**

Before working on the labs, follow the
[setup guide](setup/README.md) and run [check_setup.ipynb](setup/check_setup.ipynb).
Choose one of four routes: local Python/Jupyter, MIN JupyterHub, Google Colab,
or the supplied Nix environment. All routes use the same lab notebooks.

This repository starts with setup information. Each lab folder will be added
before its class. You can complete all setup checks now, without any
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
[Git guide](setup/git.md). Work in your copy of `lab_01.ipynb`, which contains
all exercise statements and homework. This notebook is the exercise sheet.
Work through the examples and tasks in order, predict what will
happen before running code, and write brief explanations alongside your
results. The notebook includes the tutorial exercises and homework and
needs no helper files. Write mathematical answers in Markdown cells, using
`$...$` for inline formulas and `$$` on separate lines around display formulas.
Press **Shift+Enter** to render a Markdown cell. Save and submit your completed
`.ipynb` with its outputs and written answers.

When **Lab 2** is released, copy the whole `lab_02` folder to
`my-work/lab_02`, keeping `lab_02_support.py` beside the notebooks. Choose
either `lab_02_guided.ipynb` (smaller subtasks, examples, and hints) or
`lab_02_independent.ipynb` (more implementation and design choices left to you).
In both versions, you write model definitions and evaluation code to build
and train a handwritten-digit recogniser with MNIST. For homework, design
your own second architecture and investigate how small random image
perturbations affect predictions. The training routine is supplied. The shared
preparation guide identifies useful PyTorch functions and explains the new
dependencies. Read it a few days before class; you are welcome to start
solving early. Colab users upload their chosen notebook and the helper file
to the runtime, and save a copy of their completed notebook separately.

At the end of Lab 2, you can also draw your own digit in an optional notebook
canvas and ask your trained network to recognise it. Follow Exercise 6 for the
optional widget setup and use its recording cell to retain the drawing and
prediction in your saved notebook. Loading a PNG/JPEG file and using the
supplied examples remain available without the drawing widget.
If a library cannot be imported, or you see
`Failed to load model class 'AnyModel' from module 'anywidget'`, follow the
[short Lab 2 troubleshooting instructions](setup/troubleshooting.md#lab-2-libraries-and-the-drawing-canvas).
You can complete the image experiment using a PNG/JPEG file when the canvas
cannot load.

For Lab 2, submit **one** chosen notebook containing both tutorial and
homework answers, code, and outputs. Both versions have the same core
requirements. You may work in groups of at most four. The teaching team gives
feedback rather than grades; follow Moodle for the deadline and submission
channel. The goal is a reasonable solution and an explanation of your work,
not a competition for the highest recognition accuracy.

Complete the setup checks before class. Lab 1 uses the CPU. Lab 2 selects
a CUDA GPU if one is available and also supports CPU computation. The supplied
Nix environment remains CPU-only. Keep an already working hosted environment;
do not install CUDA or replace its PyTorch packages just to run these labs.



