{% if cookiecutter.use_mkdocs == 'y' %}
#!/usr/bin/env python
"""
Script to automatically generate API documentation for the project.
This creates markdown files for each module in the project.
"""
import os
import pkgutil
import importlib
from pathlib import Path

# Configuration
PACKAGE_NAME = "{{ cookiecutter.project_slug }}"
API_DOCS_DIR = Path("docs/api")


def generate_module_docs(module_name, api_dir):
    """Generate documentation for a module."""
    # Create the output file path
    rel_path = module_name.replace(f"{PACKAGE_NAME}.", "").replace(".", "/")
    output_path = api_dir / f"{rel_path}.md"
    
    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create the markdown content
    content = f"# {module_name}\n\n::: {module_name}\n"
    
    # Write the content to the file
    with open(output_path, "w") as f:
        f.write(content)
    
    print(f"Generated docs for {module_name} at {output_path}")


def discover_modules(package_name):
    """Discover all modules in the package."""
    package = importlib.import_module(package_name)
    modules = [package_name]
    
    if hasattr(package, "__path__"):
        for _, name, is_pkg in pkgutil.iter_modules(package.__path__, f"{package_name}."):
            modules.append(name)
            if is_pkg:
                modules.extend(discover_modules(name))
    
    return modules


def main():
    """Main function to generate API documentation."""
    # Ensure the API docs directory exists
    api_dir = Path(API_DOCS_DIR)
    api_dir.mkdir(parents=True, exist_ok=True)
    
    # Discover all modules
    modules = discover_modules(PACKAGE_NAME)
    
    # Generate documentation for each module
    for module_name in modules:
        try:
            generate_module_docs(module_name, api_dir)
        except Exception as e:
            print(f"Error generating docs for {module_name}: {e}")


if __name__ == "__main__":
    main()
{% endif %}
