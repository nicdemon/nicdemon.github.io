# Configuration file for the Sphinx documentation builder.
import sys
from pathlib import Path

sys.path.append(str(Path('_ext').resolve()))

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Nicolas de Montigny - Portfolio'
copyright = '2025, Nicolas de Montigny'
author = 'Nicolas de Montigny'
release = '2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx_design',
    'sphinx_new_tab_link',
    'ablog',
    'myst_nb',
    'blogpost'
]

templates_path = ['_templates']
exclude_patterns = []
myst_update_mathjax = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Nicolas de Montigny - Portfolio'
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_theme_options = {
    "secondary_sidebar_items":[],
    "icon_links":[
        {"name": "Github", "url": "https://github.com/nicdemon", "icon": "fa-brands fa-square-github"},
        {"name": "LinkedIn", "url": "https://linkedin.com/in/nicolas-de-montigny-8755101b0", "icon": "fa-brands fa-linkedin"},
        {"name": "ResearchGate", "url": "https://www.researchgate.net/profile/Nicolas-De-Montigny", "icon": "fa-brands fa-researchgate"},
        {"name": "OrcID", "url": "https://orcid.org/0000-0002-3708-4055", "icon": "fa-brands fa-orcid"}
    ],
    "icon_links_label": "Quick Links"
}
html_sidebars = {
    "*": []
}
html_favicon = "img/favicon.ico"
# html_extra_path = ["feed.xml"]

# -- Options for ABlog output -------------------------------------------------
# https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html

blog_post_pattern = [
    "posts/genomics/*.md",
    "posts/interfaces/*.md",
    "posts/training/*.md",
    "posts/cv-info/*.md"
]
blog_authors = {
    "Nicolas": ("Nicolas de Montigny","https://nicdemon.github.io/")
}
blog_default_author = "Nicolas"
post_date_format = "%d/%m/%y"

# -- ABlog ---------------------------------------------------

# blog_baseurl = "https://nicdemon.github.io/"
# blog_title = "Nicolas de Montigny"
# blog_path = "posts"
# blog_post_pattern = "posts/*/*"
# blog_feed_fulltext = True
# blog_feed_subtitle = ""
# fontawesome_included = True
# post_redirect_refresh = 1
# post_auto_image = 1
# post_auto_excerpt = 2

# -- MyST and MyST-NB ---------------------------------------------------

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# MyST-NB
nb_execution_mode = "off"

# Sphynx app setup
def setup(app):
    # app.add_directive("blogpost", BlogPost)
    app.add_css_file("custom.css")