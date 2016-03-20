# -*- coding: utf-8 -*-

import re

from lxml import etree


def parse_html(html):
    parser = etree.HTMLParser()

    return etree.fromstring(html, parser=parser)


def render_html(node):
    return etree.tostring(node)


def truncate_html(html, limit):
    # truncate the document (stripped) till the end of line matching the limit
    truncate_pos = html.strip().find('\n', limit)

    if truncate_pos != -1:
        truncated_html = html[:truncate_pos]
    else:
        return html

    element = parse_html(truncated_html)
    fixed_html = render_html(element.find("body"))

    # drop opening <body> tag
    return strict_html(fixed_html[6:])


def strict_html(html):
    # swap standard '<br>' and '<hr>' tags
    return re.sub(r"(br|hr)[ ]?/", r"\1", html)


def std_html(config, page, templ_vars):
    content = strict_html(templ_vars['page']['content'])
    templ_vars['page']['content'] = content

    if 'index' in templ_vars['page']:
        char_limit = templ_vars['page']['index']['char_limit']
    else:
        # default
        char_limit = 300

    if templ_vars['pagination']['num_pages'] > 1:
        for page in templ_vars['pagination']['page_items']:
            page['content_trunc'] = truncate_html(page['content'], char_limit)
