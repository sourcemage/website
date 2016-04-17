#!/usr/bin/python
# -*- coding: utf-8 -*-

from flup.server.fcgi import WSGIServer
import hatta

config = hatta.WikiConfig(
    site_name = 'Source Mage GNU/Linux',
    front_page = 'About',
    pages_path = '/srv/www/smgl/pages',
    cache_path = '/srv/www/smgl/cache',
    template_path = '/srv/www/smgl/templates',
    pygments_style = 'autumn',
    subdirectories = True
)

config.parse_args()
config.parse_files()
config.sanitize()
wiki = hatta.Wiki(config)

WSGIServer(wiki.application).run()
