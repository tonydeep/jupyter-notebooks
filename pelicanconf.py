#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Filipe Fernandes'

SITENAME = u'python4oceanographers'
SITESUBTITLE = u'Turning ripples into waves'
# Change in publishconf.py and ignore the WARNING.  This is needed so you
# can inspect the site using a web-server at locahost.
SITEURL = ''

# Times and dates.
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'en'

# Set the article URL.
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options.
uri = 'http://ocefpaf.github.io'
MENUITEMS = [('Blog', '%s/python4oceanographers' % uri),
             ('Archives', '%s/python4oceanographers/archives.html' % uri),
             ('About', '%s/homepage' % uri),
             ]
NEWEST_FIRST_ARCHIVES = True

# Github include settings.
# GITHUB_USER = 'ocefpaf'
# GITHUB_REPO_COUNT = 0
# GITHUB_SKIP_FORK = True
# GITHUB_SHOW_USER_LINK = True

# Sidebar image
# SIDEBAR_IMAGE: Adds specified image to sidebar. Example value: "images/author_photo.jpg"
# SIDEBAR_IMAGE_ALT: Alternative text for sidebar image
# SIDEBAR_IMAGE_WIDTH: Width of sidebar image
# SEARCH_BOX: set to true to enable site search box
# SITESEARCH:

# Blogroll.
LINKS = (('PyAOS', 'http://pyaos.johnny-lin.com/'),
         ('EarthPy', 'http://earthpy.org/'),
         ('PyHOGs', 'http://pyhogs.github.io/'),
         ('drclimate', 'http://drclimate.wordpress.com/'),
         ('Software Carpentry',
          'http://software-carpentry.org/blog/index.html'),)

# Social widget.
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# STATIC_OUT_DIR requires pelican 3.3+.
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plug-ins.
THEME = 'pelican-octopress-theme'
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# The theme file should be updated so that the base header contains the line:
# {% if EXTRA_HEADER %}
# {{ EXTRA_HEADER }}
# {% endif %}

EXTRA_HEADER = open('_nb_header_mod.html').read().decode('utf-8')

# Sharing
TWITTER_USER = 'ocefpaf'
GOOGLE_PLUS_USER = '116220614704100857098'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# RSS/Atom feeds
FEED_ATOM = 'atom.xml'
FEED_DOMAIN = 'http://ocefpaf.github.io/python4oceanographers/'
FEED_MAX_ITEMS = 5

# Search
SEARCH_BOX = True

# Ignore HTMLs.
READERS = {'html': None}
