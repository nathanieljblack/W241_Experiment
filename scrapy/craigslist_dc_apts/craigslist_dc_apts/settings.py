# -*- coding: utf-8 -*-

# Scrapy settings for craigslist_sf_apts project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'craigslist_dc_apts'

SPIDER_MODULES = ['craigslist_dc_apts.spiders']
NEWSPIDER_MODULE = 'craigslist_dc_apts.spiders'

# local additions
LOG_LEVEL = 'WARNING'
FEED_FORMAT = 'csv'
FEED_URI = 'apts_dc_%(time)s.csv'

AUTOTHROTTLE_ENABLED = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist_dc_apts (+http://www.yourdomain.com)'
