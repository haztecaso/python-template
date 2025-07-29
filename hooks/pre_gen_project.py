#!/usr/bin/env python3

import re
import sys

module_name = "{{ cookiecutter.project_slug }}"

if not re.match(r"^[_a-zA-Z][_a-zA-Z0-9]+$", module_name):
    print(f"ERROR: The project slug '{module_name}' is not a valid python module name.")
    sys.exit(1)
