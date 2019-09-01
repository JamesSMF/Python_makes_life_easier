import scrapy

class BrickSetSpider(scrapy.Spider):
   name = "brickset_spider"
   allowed_domains = ['blog.scrapinghub.com']
   start_urls = ['https://blog.scrapinghub.com']


   #  def start_requests(self):
      #  yield scrapy.Request(
         #  "http://www.techbrood.com/",
         #  headers={'User-Agent': "your agent string"}
      #  )

      #  yield scrapy.Request(
         #  item['https://brickset.com/sets/year-2016'],
         #  meta = {
            #  'dont_redirect': True,
            #  'handle_httpstatus_list': [302]
         #  }, callback=self.your_callback)

   def parse(self, response):
      #  #Extracting the content using css selectors
      #  titles = response.css('.title.may-blank::text').extract()
      #  votes = response.css('.score.unvoted::text').extract()
      #  times = response.css('time::attr(title)').extract()
      #  comments = response.css('.comments::text').extract()

      #  #Give the extracted content row wise
      #  for item in zip(titles,votes,times,comments):
         #  #create a dictionary to store the scraped info
         #  scraped_info = {
            #  'title' : item[0],
            #  'vote' : item[1],
            #  'created_at' : item[2],
            #  'comments' : item[3],
         #  }

         #  #yield or give the scraped info to scrapy
         #  yield scraped_info

      SET_SELECTOR = '.set'
      PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
      MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
      IMAGE_SELECTOR = 'img ::attr(src)'

      for brickset in response.css(SET_SELECTOR):
         NAME_SELECTOR = 'h1 ::text'
         yield {
            'name': brickset.css(NAME_SELECTOR).extract_first(),
            'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
            'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
            'image': brickset.css(IMAGE_SELECTOR).extract_first(),
         }
