#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python bendruomenė'
SITENAME = u'PyCon LT'
SITEURL = ''

TIMEZONE = 'Europe/Vilnius'

DEFAULT_LANG = u'lt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

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
