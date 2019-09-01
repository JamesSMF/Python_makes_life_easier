# -*- coding: utf-8 -*-
import scrapy

class BlogbotSpider(scrapy.Spider):
   name = 'blogbot'
   allowed_domains = ['blog.scrapinghub.com']
   start_urls = ['https://blog.scrapinghub.com']
   #  allowed_domains = ['www.reddit.com/r/girls/']
   #  start_urls = ['https://www.reddit.com/r/girls/']
   #  allowed_domains = ['/quotes.toscrape.com']
   #  start_urls = ['http://quotes.toscrape.com']

   #  def start_requests(self):
      #  yield scrapy.Request(
         #  "http://quotes.toscrape.com",
         #  headers={'User-Agent': "your agent string"}
      #  )

   def parse(self, response):
      for title in response.css('.post-header>h2'):
         yield {'title': title.css('a ::text').get()}

      for next_page in response.css('a.next-posts-link'):
         yield response.follow(next_page, self.parse)
