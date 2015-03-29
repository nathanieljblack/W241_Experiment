# -*- coding: utf-8 -*-

# Scrapy settings for craigslist_sf_apts project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'chicago'

SPIDER_MODULES = ['chicago.spiders']
NEWSPIDER_MODULE = 'chicago.spiders'

# local additions
FEED_FORMAT = 'csv'
FEED_URI = 'chicago_%(time)s.csv'

AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 1
LOG_FILE = 'scrapy.log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist_dc_apts (+http://www.yourdomain.com)'
