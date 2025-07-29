{% if cookiecutter.use_mkdocs == 'y' %}
# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

## Development

To set up this project for local development:

1. Clone the repository:
   ```bash
   git clone https://github.com/{{ cookiecutter.__gh_slug }}.git
   cd {{ cookiecutter.project_slug }}
   ```

2. Set up your development environment:
   ```bash
   # Using uv (recommended)
   uv sync --all-extras --dev

   # Or using pip
   pip install -e ".[dev]"
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Testing

Run tests using pytest:

```bash
pytest
```

## Documentation

Build the documentation locally:

```bash
mkdocs serve
```

Then open `http://127.0.0.1:8000/` in your browser.
{% endif %}
