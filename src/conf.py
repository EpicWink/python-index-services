"""Sphinx configuration."""

project = "Python package index services"
author = "Laurie O"
copyright = "2023, Laurie O"
version = "1.0"
release = "1.0"

extensions = [
    "myst_parser",
]

html_copy_source = False
html_theme = "furo"
html_title = "Python package index services"
html_sidebars = {"**": []}
html_use_index = False
