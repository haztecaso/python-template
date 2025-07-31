# Python Project Template

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10_|_3.11_|_3.12_|_3.13-blue?logo=python&logoColor=white)
![Nix Flakes](https://img.shields.io/badge/Nix-Flakes-blue?logo=nixos&logoColor=white)
![uv](https://img.shields.io/badge/Package_Manager-uv-blue)
[![Tests](https://img.shields.io/badge/CI-Tests-green?logo=github&logoColor=white)](https://github.com/haztecaso/python-template/actions)

</div>

A modern cookiecutter template for Python projects using `uv` as the package manager, Nix flakes for reproducibility, and a clean development setup.

## 🚀 Usage

### Creating a new project

If you want to keep your project in sync with this template, you can use
*cruft*.

```bash
cruft create gh:haztecaso/python-template
```

Otherwise you can stick with *cookiecutter*.

```bash
cookiecutter gh:haztecaso/python-template
```

## Features

### Current Features

- 📦 **Package Management**: Modern dependency management with `uv`
- ❄️ **Reproducible Builds**: Environment consistency via nix flakes
- 🧪 **Testing**: Comprehensive testing setup with pytest
- 🧹 **Code Quality**: Automatic formatting and linting with:
  - Black for consistent code style
  - isort for organized imports
  - flake8 for code quality checks
  - pyright for static type checking
- 🪝 **Git Hooks**: Automated quality checks with pre-commit
- 📝 **Conventional Commits**: Standardized commit messages with commitizen
- 🤖 **CI Pipeline**: GitHub Actions workflow for automated testing
- 🧰 **CLI Support**: Optional command-line interface scaffolding with click or argparse
- 📚 **Documentation**: Optional MkDocs setup with automatic API documentation generation and GitHub Pages deployment

### ⏳ Planned Features
- 🛠️ **Application Patterns**:
  - Configuration management with Pydantic settings
  - Secrets management best practices
  - Observability stack (structured logging, OpenTelemetry)
- 🧩 **Framework Integrations**:
  - FastAPI for web APIs
  - SQLModel + Alembic for database access and migrations
  - Celery for background tasks
- 🐳 **Containerization**: Dockerfile and docker-compose setup
- 🔄 **Enhanced CI**: GitHub Action test matrix for multi-environment testing
- 🐍 **PyPy**: Registry setup and GitHub Action for multi-interpreter testing
