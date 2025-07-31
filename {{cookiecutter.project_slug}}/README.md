# {{ cookiecutter.project_name }}

<div align="center">
<em>{{ cookiecutter.project_short_description }}</em>
</div>

<div align="center">
<a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/test.yml/badge.svg" alt="test badge">
</a>
</div>

---

{% if cookiecutter.use_mkdocs == 'y' %}
[**Documentation**](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_slug}})
{%- endif %}
