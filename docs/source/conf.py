# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "OospCpp"
copyright = "2023-2026, Matthias Möller"
author = "Matthias Möller"
release = "2026"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

extensions = ["myst_parser"]


templates_path = ["_templates"]
exclude_patterns = []

pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_title  = "Object-oriented scientific programming with C++"
html_static_path = ["_static"]

