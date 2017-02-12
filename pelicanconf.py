#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kazuya Gosho'
SITENAME = 'Japan Life'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = './themes/Flex'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


SITESUBTITLE = "Introduce Foreigner's Life in Japan"

SITELOGO = SITEURL + '/images/profile.jpg'


DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
              'inspired by crowsfoot and clean-blog, powered by Bootstrap.'
ICONS = (
    ('github', 'https://github.com/nairobilug/pelican-alchemy'),
)
PYGMENTS_STYLE = 'default'

PYGMENTS_STYLE = 'default'

RFG_FAVICONS = True
