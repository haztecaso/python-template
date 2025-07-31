#!/usr/bin/env bash

set -e

# Remove MkDocs files if not using MkDocs
if [ "{{ cookiecutter.use_mkdocs }}" != "y" ]; then
  echo "Removing MkDocs files..."
  rm -rf docs mkdocs.yml
  rm -rf .github/workflows/docs.yml
fi

uv sync --dev
uv run black src tests
uv run isort src tests
nix build
git init --initial-branch=main && git add .
uv run pre-commit install --hook-type commit-msg --hook-type pre-commit
