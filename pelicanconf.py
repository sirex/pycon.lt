#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import timedelta

from jinja2.ext import Extension


LIVERELOAD = True

AUTHOR = u'Python bendruomenė'
SITENAME = u'PyCon LT'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Vilnius'

DEFAULT_LANG = u'lt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'
ARTICLE_EXCLUDES = ('pages', 'partials', 'images')

PAGE_URL = '{slug}.html',
PAGE_SAVE_AS = '{slug}.html'

STATIC_SAVE_AS = '{path}'
STATIC_URL = '{path}'
STATIC_PATHS = [
    'media',
    'images',
]

PLUGIN_PATHS = ['plugins']
# PLUGINS = ['assets']


class Timetable:

    def __init__(self, hours, minutes=0):
        self.time = timedelta(hours=hours, minutes=minutes)

    def __call__(self, minutes):
        starts = str(self.time)[:5]
        self.time += timedelta(minutes=minutes)
        return starts


class PyConLTExtension(Extension):
    # a set of names that trigger the extension.
    tags = set(['cache'])

    def __init__(self, environment):
        super(PyConLTExtension, self).__init__(environment)
        environment.globals.update({
            'Timetable': Timetable,
        })


JINJA_EXTENSIONS = [
    PyConLTExtension,
]
