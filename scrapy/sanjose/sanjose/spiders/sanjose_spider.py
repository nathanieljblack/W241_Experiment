from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http.request import Request
from sanjose.items import SanJoseItem
import datetime
from dateutil import parser

class SanJoseSpider(CrawlSpider):
    name = 'sanjose'
    allowed_domains = ["sfbay.craigslist.org"]
    base_url = "http://sfbay.craigslist.org"
    start_urls = ["http://sfbay.craigslist.org/search/sby/apa?srchType=T&bedrooms=1&bathrooms=1"]
    rules = [
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="content"]//a[@class="button next"]')), callback='parse_listings', follow=True)
    ]

    def parse_listings(self, response):
        today = datetime.datetime.now()
        since = today - datetime.timedelta(days=1)
        rows = Selector(response).xpath('//p[@class="row"]')
        items = []
        for row in rows:
            datestr = self.getString(row.xpath('.//span[@class="pl"]/time/@datetime').extract())
            date = parser.parse(datestr)
            if (date > since):
                item = SanJoseItem()
                item['location'] = self.getString(row.xpath('.//span[@class="l2"]/span[@class="pnr"]/small/text()').extract())
                item['housing'] = self.getString(row.xpath('.//span[@class="l2"]/span[@class="housing"]/text()').extract())
                item['title'] = self.getString(row.xpath('.//span[@class="pl"]/a[@class="hdrlnk"]/text()').extract())
                item['url'] = self.base_url + self.getString(row.xpath('.//a/@href').extract())
                item['price'] = self.getString(row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract())
                item['date'] = self.getString(row.xpath('.//span[@class="pl"]/time/@datetime').extract())
                item['posting_id'] = self.getString(row.xpath('.//@data-pid').extract())
                request = Request(item['url'], callback=self.parse_individual)
                request.meta['item'] = item
                yield request

    def parse_individual(self, response):
        item = response.meta['item']
        reply_url = self.base_url + self.getString(response.xpath('.//span[@class="replylink"]/a/@href').extract())
        request = Request(reply_url, callback=self.parse_reply)
        request.meta['item'] = item
        yield request

    def parse_reply(self, response):
        item = response.meta['item']
        item['email'] = self.getString(response.xpath('.//li/a[@class="mailapp"]/text()').extract())
        return item

    def getString(self, field):
        if (type(field) == list and len(field)!= 0):
            return field[0].encode('utf-8')
        return ""
