# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTest01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 自定义爬取的字段
    title = scrapy.Field()  # 文章标题
    author = scrapy.Field()  # 作者
    tags = scrapy.Field()  # 标签

