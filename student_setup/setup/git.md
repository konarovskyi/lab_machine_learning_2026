# Git: get the course materials and keep them up to date

Git keeps track of files and their history. A **repository** is a project
managed by Git. For this course, you only need to download the student
repository once (**clone**) and fetch new materials later (**pull**).
Initially it contains setup information. Each lab folder will appear shortly
before the corresponding class.

## 1. Get Git and make your first copy

Check whether Git is installed by entering `git --version` in a terminal.
If needed, follow the [official installation instructions](https://git-scm.com/install/).
On Windows, use **Git Bash**, which comes with Git for Windows, for the
commands below. On macOS or Linux, use your terminal.

Open a terminal in the folder where you want to keep the course materials.
Replace `REPOSITORY_URL` below with the student repository's HTTPS clone URL
provided on Moodle. Do not type the placeholder literally.

```bash
git clone REPOSITORY_URL ml-labs
cd ml-labs
```

The new `ml-labs` directory is your **course folder**. `cd` changes the
terminal's current directory. Run the remaining commands from this course
folder. Cloning is needed only once per laptop or hosted environment.

## 2. Keep your own work separate

Keep the distributed notebooks unchanged and work on copies. Before running
the setup notebook, make your copy:

```bash
mkdir -p my-work
cp setup/check_setup.ipynb my-work/check_setup.ipynb
```

Open `my-work/check_setup.ipynb` in Jupyter. Follow your chosen setup route
to install packages using the original `setup/requirements.txt`.

When a lab is released, copy its **whole folder** before starting it.
Lab 1 contains the exercise PDF, notebook, and requirements file; it needs
no Python helper files. Once `lab_01` is available:

```bash
cp -R lab_01 my-work/
```

Then work in `my-work/lab_01`. Copy a lab only once; do not copy over a folder
containing your answers. If corrections are published, compare the updated
original with your working copy. For package updates, use the original lab's
requirements file from the course root, following that lab's instructions.

The supplied `.gitignore` excludes `my-work/` from Git tracking. Your answers
therefore do not interfere with course updates. Save them regularly and keep
a backup: Git does not back up this ignored folder.

## 3. Get updates before each class

Open a terminal in your `ml-labs` course folder and check:

```bash
git status --short
```

No output means Git sees no changes to tracked files or unignored new files.
Then update:

```bash
git pull --ff-only
```

This downloads newly released folders and corrections. The `--ff-only`
option stops if your local history has diverged instead of merging it.

If the status lists changed files or an update fails, keep your work and
ask for help with the full message. Do not use `git reset --hard` to fix it.

You do not need `git commit` or `git push` for this workflow. Pulling updates
does not submit homework; follow the submission instructions on each sheet.

## Hosted environments

On MIN JupyterHub, you can use the same commands in its terminal. For Colab,
you can download and upload the required files without Git; see the
[Colab guide](colab.md).

Official command references: [clone](https://git-scm.com/docs/git-clone),
[status](https://git-scm.com/docs/git-status),
[pull](https://git-scm.com/docs/git-pull).
