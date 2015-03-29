# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ChicagoItem(Item):
    # define the fields for your item here like:
    title = Field()
    url = Field()
    price = Field()
    date = Field()
    location = Field()
    housing = Field()
    email = Field()
    posting_id = Field()
