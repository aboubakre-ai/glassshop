import scrapy


class GlasseshopSpider(scrapy.Spider):
    name = 'glasseshop'
    allowed_domains = ['www.glassesshop.com']
    #start_urls = ['https://www.glassesshop.com/bestsellers']

    def start_requests(self):
        yield scrapy.Request(url="https://www.glassesshop.com/bestsellers",
        headers={ 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        })

    def parse(self, response):

       for product in response.xpath("//div[contains(@class,'product-list-item') and not(contains(@class,'ad-banner'))]"):
            yield{
            'url': product.xpath(".//div[@class='product-img-outer']/a/@href").get(),
            'image_link': product.xpath(".//div[@class='product-img-outer']/a/img[2]/@data-src").get(),
            'name' : product.xpath(".//div[@class='p-title']/a/text()").get().strip(),
            'price' : product.xpath(".//div[@class='p-price']/div/span/text()").get().strip(),
            }

       next_page = response.xpath("//a[@rel='next']/@href").get()
       if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
            })

  
   