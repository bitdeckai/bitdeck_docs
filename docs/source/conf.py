# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'bitdeck'
copyright = '2025, bitdeck'
author = 'bitdeck'

release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# 添加以下配置，设置导航栏默认展开
# 修改主题选项
html_theme_options = {
    # 导航选项
    'collapse_navigation': True,     # 改为 True，允许折叠
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_show_sourcelink = False  # 禁用查看源码链接

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_static_path = ['_static']

extensions = [
    'sphinx_tabs.tabs'
]
