# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme
import sphinx_book_theme

sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'CyberGIS-Vis-Documentation'
copyright = '2022, Chaeyeon Han'
author = 'Chaeyeon Han'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = ['myst_parser']
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_theme_path = [sphinx_book_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
    "repository_url": "https://github.com/bravoyourlif/CyberGIS-Vis-Documentation2", # git repository url
    "use_repository_button": True, #show git repository
    "toc_title": "Contents", #title of right side bar
    "show_toc_level": 2,  # level of right side bar
    "use_download_button": True, # allow user to download the page in raw, pdf, or ipynb if available.
    "use_issues_button": True,
    "use_edit_page_button": True,
}
html_logo = "cybergis-vis-image.png" #logo that shows on the top left corner
#html_title = "CyberGIS-Vis Documentation" #this goes under the logo
html_sidebars = { # side bar configuration
    "**": ["sidebar-logo.html", "search-field.html","sbt-sidebar-nav.html"] # ** indicates configuration that applies to ALL pages.
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]
