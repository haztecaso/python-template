#!/usr/bin/env bash

set -e

uv sync --dev
uv run black src tests
uv run isort src tests
nix build
git init && git branch -m "main" && git add .
uv run pre-commit install --hook-type commit-msg --hook-type pre-commit 
