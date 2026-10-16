# Route 4: Nix

[Back to the setup guide](README.md)

Use this route if you already use Nix. The supplied flake currently targets
**`x86_64-linux`**, including NixOS on that architecture. It is not a ready-made
environment for macOS, Windows, or ARM Linux; use one of the other routes there.
You do not need to install Nix just for this course.

Open a terminal in the **course folder**, the root of your student repository
copy. Keep both `flake.nix` and `flake.lock` there.

```bash
nix develop
jupyter lab
```

The shell should show `(ml-labs)`. Copy `setup/check_setup.ipynb` into a
`my-work` folder at the course root, open that copy in JupyterLab, select
Python, and run the required checks. No lab folder is needed yet.

If Nix reports that the `nix-command` or `flakes` feature is disabled, enable
them for this invocation:

```bash
nix --extra-experimental-features "nix-command flakes" develop
jupyter lab
```

The first run can take time while Nix obtains packages. The existing flake
provides JupyterLab, ipykernel, NumPy, and Matplotlib. Use this environment
directly; a separate `.venv` and pip installation are unnecessary for Lab 1.
Keep the supplied lock file so that the Nix input remains pinned. Do not run
`nix flake update` as part of the student setup.

After stopping JupyterLab, type `exit` to leave the development shell. For the
next session, return to this folder and run `nix develop` again. Additional
packages and corresponding environment updates will be announced with later
labs. This flake does not configure CUDA or install PyTorch.

Official reference: [nix develop](https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-develop).
