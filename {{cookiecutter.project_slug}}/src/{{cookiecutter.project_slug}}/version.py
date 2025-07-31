"""Utilities to retrieve the information of the program version."""

# Do not edit the version manually, let `cz bump` do it.
__version__ = "0.1.0"


def version_info() -> str:
    import platform
    import sys
    from textwrap import dedent
    """Display the version of the program, python and the platform."""
    return dedent(
        f"""\
        ------------------------------------------------------------------
             {{cookiecutter.project_slug}}: {__version__}
             Python: {sys.version.split(" ", maxsplit=1)[0]}
             Platform: {platform.platform()}
        ------------------------------------------------------------------"""
    )

if __name__ == "__main__":
    print(version_info())
