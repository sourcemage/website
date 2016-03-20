#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import re
from cStringIO import StringIO

from flup.server.fcgi import WSGIServer

import Image, ImageDraw, ImageFont


_FONT_PATH = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
_FONT_SIZE = 12
_FONT_COLOR = "#d24f4f"
_BG_COLOR = "#ffffff"
_OFFSET = (2, 2)
_FORMAT = "PNG"
_ERROR_IMAGE = "static/error.png"
_LIMIT = 100

wsgi_opts = {
    'debug': False
}


def MageHandler(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8'),
               ('Server', 'Source Mage Mail Address GEnerator')]

    pattern = r"addr=([^&]+)"
    address = re.compile(pattern).search(environ['QUERY_STRING'])

    if address and len(address.group(1)) < _LIMIT:
        try:
            message = base64.b64decode(address.group(1)).decode('utf-8')
        except:
            message = "Decoding error"

        if message:
            headers[0] = ('Content-Type', 'image/png')

            try:
                font = ImageFont.truetype(_FONT_PATH, _FONT_SIZE)
                size = [i.__add__(_OFFSET[0]) for i in font.getsize(message)]

                image = Image.new("RGB", size, _BG_COLOR)
                draw = ImageDraw.Draw(image)
                draw.text(_OFFSET, message, font=font, fill=_FONT_COLOR)

                output = StringIO()
                image.save(output, _FORMAT)
                message = output.getvalue()
                output.close()
            except:
                error = open(_ERROR_IMAGE)
                message = error.read()
                error.close()
    else:
        message = "Usage: http://%s?addr=base64-string" % environ['HTTP_HOST']

    start_response('200 OK', headers)

    return [message]


if __name__ == '__main__':
    WSGIServer(MageHandler, **wsgi_opts).run()
