{% if cookiecutter.use_mkdocs == 'y' %}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

## Usage

```python
from {{ cookiecutter.project_slug }} import example

# Add usage examples here
```

## Features

* Add your project features here

## License

{{ cookiecutter.open_source_license }}
{% endif %}
