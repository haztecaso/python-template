#!/usr/bin/env bash

set -e

uv sync --dev
nix build
