So you've started using `{{ cookiecutter.project_slug }}` and want to show your
gratitude to the project, depending on your programming skills there are
different ways to do so.

# I don't know how to program

There are several ways you can contribute:

- [Open an issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues/new) if you encounter
    any bug or to let us know if you want a new feature to be implemented.
- Spread the word about the program.
- Review the [documentation](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}) and try to improve
    it.

# I know how to program in Python

If you have some python knowledge there are some additional ways to contribute.
We've ordered the [issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues) in
[milestones](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/milestones), check the issues in
the smaller one, as it's where we'll be spending most of our efforts. Try the
[good first
issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22),
as they are expected to be easier to get into the project.

We develop the program with
[TDD](https://en.wikipedia.org/wiki/Test-driven_development), so we expect any
contribution to have it's associated tests. We also try to maintain an updated
[documentation](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}) of the project, so think if
your contribution needs to update it.

We know that the expected code quality is above average. Therefore it might
be changeling to get the initial grasp of the project structure, know how to make the
tests, update the documentation or use all the project technology stack. but please
don't let this fact discourage you from contributing:

- If you want to develop a new feature, explain how you'd like to do it in the related issue.
- If you don't know how to test your code, do the pull request without the tests
    and we'll try to do them for you.

# Issues

Questions, feature requests and bug reports are all welcome as issues.
**To report a security vulnerability, please see our [security
policy](https://github.com/{{ cookiecutter.github_username }}/{{
cookiecutter.project_slug }}/security/policy) instead.**

To make it as simple as possible for us to help you, please include the output
of the following call in your issue:

```bash
uv run src/{{ cookiecutter.project_slug }}/version.py
```

Please try to always include the above unless you're unable to install `{{
cookiecutter.project_slug }}` or know it's not relevant to your question or
feature request.

# Pull Requests

*{{ cookiecutter.project_slug }}* is released regularly so you should see your
improvements release in a matter of days or weeks.

!!! note
    Unless your change is trivial (typo, docs tweak etc.), please create an
    issue to discuss the change before creating a pull request.

If you're looking for something to get your teeth into, check out the ["help
wanted"](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)
label on github.

# Development facilities

To make contributing as easy and fast as possible, you'll want to run tests and
linting locally.

You'll need to have python 3.10, 3.11, 3.12, or 3.13, uv and git installed. The
nix package manager is also recommended.

* Clone your fork and go into the repository directory:

    ```bash
    git clone git@github.com:<your username>/{{ cookiecutter.project_slug }}.git
    cd {{ cookiecutter.project_slug }}
    ```

* Set up the virtualenv for running tests:

    ```bash
    uv sync
    source env/bin/activate
    ```

* Checkout a new branch and make your changes:

    ```bash
    git checkout -b my-new-feature-branch
    ```

* Fix formatting and imports: {{ cookiecutter.project_slug }} uses
    [black](https://github.com/ambv/black) to enforce formatting and
    [isort](https://github.com/timothycrosley/isort) to fix imports.

    ```bash
    uv run black
    ```

* Run tests and linting:

    ```bash
    uv run pre-commit
    ```

    There are more sub-commands in Makefile like `test-code`, `test-examples`,
    `mypy` or `security` which you might want to use, but generally `make`
    should be all you need.

    If you need to pass specific arguments to pytest use the `ARGS` variable,
    for example `make test ARGs='-k test_markdownlint_passes'`.

* Build documentation: If you have changed the documentation, make sure it
    builds the static site. Once built it will serve the documentation at
    `localhost:8000`:

    ```bash
    mkdocs serve
    ```

* Commit, push, and create your pull request.

* Make a new release: To generate the changelog of the new changes, build the
    package, upload to pypi and clean the build files use `make bump`.

We'd love you to contribute to *{{ cookiecutter.project_slug }}*!
