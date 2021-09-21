# Honknet - Sphinx Configuration File
# Configuration file for the Sphinx documentation builder.

#   [ Project ]

project = "Honknet"
copyright = "2021; iiPython + DmmD"
author = "iiPython, DmmD"

#   [ General Configuration ]
extensions = ["myst_parser"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

#   [ HTML Configuration ]
html_theme = "basic"
html_static_path = ["_static"]
html_style = "style.css"
html_title = "Honknet"
html_favicon = "_images/favicon.ico"
