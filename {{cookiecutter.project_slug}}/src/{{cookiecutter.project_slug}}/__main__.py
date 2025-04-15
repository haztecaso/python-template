{%- if cookiecutter.command_line_interface.lower() == "click" %}
import click

@click.command()
def main():
    """Console script for {{ cookiecutter.project_slug }}."""
    click.echo("Hello from {{ cookiecutter.project_name }}")
{%- else %}
def main():
    """Console script for {{ cookiecutter.project_slug }}."""
    print("Hello from {{ cookiecutter.project_name }}")
{%- endif %}

if __name__ == "__main__":
    main()

