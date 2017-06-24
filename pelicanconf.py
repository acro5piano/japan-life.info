#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kazuya Gosho'
SITENAME = 'Japan Life'
SITEURL = 'http://japan-life.info'

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
LINKS = (('About us', '/about-us.html'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = './themes/Flex'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITESUBTITLE = "プログラミング、Airbnb運営、台湾人彼女、その他雑多なことを書き残す"

SITELOGO = SITEURL + '/images/profile.jpg'

SITEDESCRIPTION = "Introduce Foreigner's Life in Japan"

STATIC_PATHS = [
    'favicon.ico',
    'images',
    'css',
]

RFG_FAVICONS = True


CUSTOM_CSS = 'css/custom.css'

PLUGIN_PATHS = ['plugins']
#PLUGINS = ['better_figures_and_images']

RESPONSIVE_IMAGES = True
