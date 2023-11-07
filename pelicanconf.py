AUTHOR = 'The Hacktionarists'
SITENAME = 'Hacktionary'
SITEURL = ''


PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

ARTICLE_ORDER_BY = 'basename'

RELATIVE_URLS = True

DISPLAY_RECENT_POSTS_ON_MENU = True

DISPLAY_PAGES_ON_MENU = False

DISPLAY_CATEGORIES_ON_MENU = False


#Theme-related elements

THEME = 'themes/pelican-twitchynary'

CC_LICENSE = 'CC-BY'

RECENT_POST_COUNT = 1000

SOCIAL = (('github', 'https://github.com/hackthackathon'), ('Discord', 'https://discord.gg/45ReWfUR'))
SITELOGO = 'images/hth3_background.jpg'
SITELOGO_SIZE = '50px'
CUSTOM_CSS = 'theme/css/hacktionary.css'
