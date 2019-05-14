#!/usr/bin/python
# -*- coding: utf-8 -*-

import hatta

from flup.server.fcgi import WSGIServer
from wsgibrotli.br import BrotliMiddleware
from wsgigzip.gzip import GzipMiddleware

config = hatta.WikiConfig(
    site_name = 'Source Mage GNU/Linux',
    front_page = 'News',
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

WSGIServer(GzipMiddleware(BrotliMiddleware(wiki.application, etag_alter=True))).run()
