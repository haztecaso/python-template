{%- if cookiecutter.command_line_interface.lower() == "click" %}
import click


@click.command()
@click.option("--name", is_flag=False, flag_value="Flag", default="O.")
def main(name):
    """Cli interface for {{ cookiecutter.project_slug }}."""
    click.echo(f"Hello {name} from {{ cookiecutter.project_name }}")
{%- elif cookiecutter.command_line_interface.lower() == "argparse" %}
import argparse


def main():
    """Cli interface for {{ cookiecutter.project_slug }}."""
    parser = argparse.ArgumentParser(prog='{{ cookiecutter.project_slug }}')
    # parser.add_argument('echo', help="echo the string you use here")
    # parser.add_argument("square", help="display a square of a given number", type=int)
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    args = parser.parse_args()

    if args.verbose: print("verbosity turned on")
    print("Hello from {{ cookiecutter.project_name }}")
    # print(f"Echo: {args.echo}")
    # print(f"The square of {args.square} is {args.square ** 2}")
{%- else %}
def main():
    """Main entrypoint for {{ cookiecutter.project_slug }}."""
    print("Hello from {{ cookiecutter.project_name }}")
{%- endif %}

if __name__ == "__main__":
    main()

