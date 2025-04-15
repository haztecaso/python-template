#!/usr/bin/env bash

set -e

uv sync
nix build
