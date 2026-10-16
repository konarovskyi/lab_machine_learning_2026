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

When a lab is released, upload its notebook in the same way. If it comes with
Python helper files, upload them separately using the runtime's **Files**
panel. Opening an `.ipynb` does not upload its companions. Uploaded runtime
files and Python variables are temporary. Saving the notebook in Drive does
not preserve those files, so re-upload companions after a new runtime starts.

NumPy and Matplotlib are normally available. If the setup check reports a
missing/outdated one, run this in a notebook cell, restart the session, and
rerun the checks:

```python
%pip install "numpy>=1.24" "matplotlib>=3.7"
```

Colab already supplies the notebook interface; do not launch a JupyterLab
server inside it. For a later GPU lab, select **Runtime > Change runtime type**
and an available GPU, then run the optional CUDA check. GPU availability varies.

Official references: [Colab FAQ](https://research.google.com/colaboratory/faq.html),
[file upload examples](https://colab.research.google.com/notebooks/io.ipynb).
