#!/usr/bin/python
# -*- coding: utf-8 -*-

from flup.server.fcgi import WSGIServer
import hatta

config = hatta.WikiConfig(
    site_name = 'Source Mage GNU/Linux',
    front_page = 'About',
    pages_path = '/var/www/smgl/web/site/pages',
    cache_path = '/var/www/smgl/web/site/cache',
    template_path = '/var/www/smgl/web/site/templates',
    pygments_style = 'autumn',
    math_url = 'mathjax',
    subdirectories = True
)

config.parse_args()
config.parse_files()
config.sanitize()
wiki = hatta.Wiki(config)

WSGIServer(wiki.application).run()
