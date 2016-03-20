#!/usr/bin/python
# -*- coding: utf-8 -*-

from flup.server.fcgi import WSGIServer
from wsgigzip.gzip import GzipMiddleware
import hatta

config = hatta.WikiConfig(
    site_name = 'Source Mage GNU/Linux',
    front_page = 'News',
    pages_path = '/var/www/smgl/pages',
    cache_path = '/var/www/smgl/cache',
    template_path = '/var/www/smgl/templates',
    pygments_style = 'autumn',
    subdirectories = True
)

config.parse_args()
config.parse_files()
config.sanitize()
wiki = hatta.Wiki(config)

WSGIServer(GzipMiddleware(wiki.application)).run()
