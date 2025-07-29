import pytest
from {{cookiecutter.project_slug}}.__main__ import main

{%- if cookiecutter.command_line_interface.lower() == "click" %}
from click.testing import CliRunner


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert result.output == "Hello from {{ cookiecutter.project_name }}\n"
{% else %}

def test_main():
    result = main()
    assert result is None
{% endif%}
