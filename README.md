# Python project template with uv, nix flakes and cookiecutter

A modern cookiecutter template for python projects using uv as the package manager, nix flakes for reproducibility, and a clean development setup. 

## Features

- 📦 Package management with uv
- ❄️ Reproducible builds via Nix flakes
- 🧪 Testing with pytest
- 🧹 Code formatting and linting with *black*, *isort*, *flake8* and *pyright*.
- 🪝 Git hooks with pre-commit
- 🤖 CI with GitHub Actions to run your tests on push
- 🧰 Optional CLI scaffolding with click

## Usage

This template is intended to be used in machines with the *nix* package manager
installed. You can install *cookiecutter* in your preferred way or create
temporal shell with it using `nix-shell -p cookiecutter`.

To use the template:

```bash
cookiecutter gh:haztecaso/python-template
```

After generation you should run the following commands in the newly created
project folder:

```bash
# if you use direnv 
direnv allow

# to activate the development environment
nix develop

# initialize the github repo
git init

# to stage the project files 
git add .

# install git hooks
pre-commit install --hook-type commit-msg --hook-type pre-commit 
```

## Roadmap

Planned features:

- 🐍 PyPy registry setup and GitHub Action for multi-interpreter testing
- 💬 typer CLI support
- 🧩 Common python application layouts.
