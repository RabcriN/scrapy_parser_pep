from urllib.parse import urlparse

import scrapy

from pep_parse.constants import START_URLS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [urlparse(*START_URLS).netloc]
    start_urls = START_URLS

    def parse(self, response):
        all_peps = response.css(
            '#numerical-index > table > tbody > tr > td:nth-child(3) > a'
        )
        for link in all_peps:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.selector.xpath(
                '//*[@id="pep-content"]/h1/text()'
            ).get().split('–')[:1][0][3:].strip(),
            'name': response.selector.xpath(
                '//*[@id="pep-content"]/h1/text()'
            ).get().split('–')[1:][0].strip(),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
