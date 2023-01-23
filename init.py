#!/usr/bin/python
# -*- coding: utf-8 -*-

import hatta

from flup.server.fcgi import WSGIServer
from wsgibrotli.br import BrotliMiddleware
from wsgigzip.gzip import GzipMiddleware


class SMGLWikiParser(hatta.WikiParser):
    """ WikiParser with support for Creole Additions from 
        http://www.wikicreole.org/wiki/CreoleAdditions """

    markup_rules = hatta.WikiParser.markup_rules
    punct = hatta.WikiParser.punct
    # replaced by subscript
    punct.pop(r",,")

    @markup_rules(r"\^\^", 41)
    def _line_superscript(self):
        if 'sup' in self.stack:
            return self.pop_to('sup')
        else:
            self.stack.append('sup')
            return "<sup>"

    @markup_rules(r",,", 42)
    def _line_subscript(self):
        if 'sub' in self.stack:
            return self.pop_to('sub')
        else:
            self.stack.append('sub')
            return "<sub>"


class SMGLWikiPageWiki(hatta.WikiPageWiki):
    
    def __init__(self, *args, **kw):
        super(SMGLWikiPageWiki, self).__init__(*args, **kw)

        self.parser = SMGLWikiParser

class SMGLWiki(hatta.Wiki):

    hatta.Wiki.mime_map['text/x-wiki'] = SMGLWikiPageWiki


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
wiki = SMGLWiki(config)

WSGIServer(GzipMiddleware(BrotliMiddleware(wiki.application, etag_alter=True))).run()
