import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest
from pytest_cookies.plugin import Cookies, Result

# Type alias
type Context = dict[str, Any]

def load_contexts() -> dict[str, Context]:
    with open(Path(__file__).parent / "contexts.json", "r") as f:
        import json
        data = json.load(f)
    assert isinstance(data, dict), "contexts.json must contain a dictionary"
    for key, value in data.items():
        assert isinstance(value, dict), f"Context '{key}' must be a dictionary"
    return data

CONTEXTS = load_contexts()


@pytest.fixture(scope="module")
def template_root() -> str:
    return str(Path(__file__).parent.parent)


@pytest.fixture
def project(
    request: pytest.FixtureRequest,
    cookies: Cookies,
    template_root: str,
) -> Result:
    """
    Fixture to bake a cookiecutter project for a given context name.
    The name is passed indirectly via parametrize.
    """
    context_name: str = request.param
    if context_name not in CONTEXTS:
        raise ValueError(f"Unknown context name: {context_name}")
    extra_context = CONTEXTS[context_name]
    return cookies.bake(extra_context=extra_context, template=template_root)


@pytest.mark.parametrize("project", ["default", "minimalist"], indirect=True)
def test_basic_generation(project: Result):
    assert project.exit_code == 0
    assert project.exception is None
    assert project.project_path is not None
    assert project.project_path.is_dir()


@pytest.mark.parametrize("project", ["click", "argparse", "minimalist"], indirect=True)
def test_main_entrypoint(project: Result):
    """Test that the main entrypoint can be run successfully."""
    project_path = project.project_path
    assert project_path is not None
    project_name = os.path.basename(project_path)

    # Run the module using Python's -m flag
    process = subprocess.run(
        ["uv", "run", project_name],
        cwd=project_path,
        capture_output=True,
        text=True,
    )

    # Check that the command executed successfully
    assert (
        process.returncode == 0
    ), f"Main entrypoint failed with error: {process.stderr}"

    # Verify expected output is present (all variants should print a welcome message)
    assert (
        f"Hello from " in process.stdout
    ), f"Expected welcome message not found in output: {process.stdout}"


@pytest.mark.parametrize("project", ["default", "minimalist"], indirect=True)
def test_pytest_runs(project: Result):
    """Test that pytest can run successfully in the generated project."""
    project_path = project.project_path
    assert project_path is not None

    test_dir = project_path / "tests"
    assert test_dir.is_dir(), f"Expected tests directory not found: {test_dir}"

    # Run pytest in the generated project
    process = subprocess.run(
        ["uv", "run", "pytest", "-xvs"],
        cwd=project_path,
        capture_output=True,
        text=True,
    )

    # Check that pytest ran successfully
    assert (
        process.returncode == 0
    ), f"pytest failed with error: {process.stderr}\nOutput: {process.stdout}"
    assert (
        "1 passed" in process.stdout
    ), f"Expected '1 passed' in pytest output, but got: {process.stdout}"
