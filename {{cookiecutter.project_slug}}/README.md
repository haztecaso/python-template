# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.use_mkdocs == 'y' %}
## Documentation

This project uses MkDocs for documentation. To build and view the documentation locally:

```bash
# Install documentation dependencies
uv sync --group docs

# Generate API documentation
python docs/gen_api_docs.py

# Serve documentation locally
mkdocs serve
```

The documentation will be available at http://127.0.0.1:8000/

When you push to the main branch, the documentation will automatically be built and deployed to GitHub Pages.
{% endif %}
