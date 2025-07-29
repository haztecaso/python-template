# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.use_mkdocs == 'y' %}
[docs](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_slug}})
{%- endif %}
