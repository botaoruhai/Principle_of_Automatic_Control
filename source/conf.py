# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Principle of Automatic Control'
copyright = '2024, botaoruhai'
author = 'botaoruhai'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

language = 'zh_CN'
extensions = ['recommonmark']
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'markdown',
#     '.md': 'markdown',
# }

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_theme = 'traditional'
html_static_path = ['_static']

