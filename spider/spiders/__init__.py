# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy


class Product(scrapy.Item):
    product_url = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
