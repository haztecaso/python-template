# {{ cookiecutter.project_name }}

<div align="center">
*{{ cookiecutter.project_short_description }}*
</div>

<div align="center">
![Test](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/test.yml/badge.svg)
</div>

---

{% if cookiecutter.use_mkdocs == 'y' %}
[**Documentation**](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_slug}})
{%- endif %}
