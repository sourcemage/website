#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2019, Vlad Glagolev <stealth@sourcemage.org>

import os
import stat
import sys

from random import random

import redis
import requests
import yaml

from bottle import route, default_app, redirect, abort, request
from flup.server.fcgi import WSGIServer


_DEFAULT_CONFIG = os.path.join(sys.path[0], "fallback.yml")

_CONFIG_FORMAT = {
    'redis': ('password', 'expiration'),
    'servers': ('name', 'url')
}


def check_mode(f):
    st = os.stat(f)

    if st.st_mode & (stat.S_IRGRP | stat.S_IROTH):
        raise Exception("configuration file is group/world-readable")


def configure(f):
    """ Check configuration file syntax. """

    try:
        fp = open(f)
    except IOError as e:
        raise Exception("unable to open configuration file '%s': %s" % (f, e))

    try:
        check_mode(fp.name)

        config = yaml.safe_load(fp)
    except yaml.YAMLError as e:
        raise Exception("syntax mismatch in configuration file '%s': %s" % (fp.name, e))
    except Exception:
        raise
    finally:
        fp.close()

    for section in _CONFIG_FORMAT:
        if section not in config:
            raise Exception("missing section: %s" % section)

        if section in ('servers',):
            if type(config[section]) != list:
                raise Exception("section '%s' must be a list" % section)

            for key in _CONFIG_FORMAT[section]:
                for item in config[section]:
                    if key not in item:
                        raise Exception("missing key in section's '%s' item: %s" % (section, key))

                    if type(item[key]) != str:
                        raise Exception("value for '%s' must be a string" % key)

        if section in ('redis',):
            if type(config[section]) != dict:
                raise Exception("redis item must be a dictionary")

            for key in _CONFIG_FORMAT[section]:
                if key not in config[section]:
                    raise Exception("missing key in section '%s': %s" % (section, key))

                if key == "password" and type(config[section][key]) != str:
                    raise Exception("value for '%s' must be a string" % key)
                elif key == "expiration" and type(config[section][key]) != int:
                    raise Exception("value for '%s' must be an integer" % key)

    return config


try:
    conf = configure(_DEFAULT_CONFIG)
except Exception as e:
    print("configuration error: %s" % e)

    sys.exit(1)
else:
    red = redis.Redis(password=conf['redis']['password'])
    servers = {s['name']: s['url'] for s in conf['servers']}


@route('/')
@route('/<args:path>')
def index(args=''):
    src = args[args.rfind('/') + 1:]

    try:
        no_redis = False
        res = red.get(src)
    except Exception:
        no_redis = True
        res = None

    if res:
        redirect(servers[res] + src)

    for mirror_id, mirror_url in sorted(servers.items(), key=lambda x: random()):
        url = mirror_url + src

        try:
            req = requests.head(url, allow_redirects=True, timeout=5)

            if req.ok:
               if not no_redis:
                   red.set(src, mirror_id, ex=conf['redis']['expiration'])

               break
        except Exception:
            req = None

            continue

    if req and req.ok:
        redirect(url)
    else:
        abort(404, "File not found")


WSGIServer(default_app()).run()
