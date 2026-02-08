"""
使用scrapy爬取 https://quotes.toscrape.com/ 网站的文章
"""

import scrapy

from scrapy_test01.items import ScrapyTest01Item

class QuotesSpider(scrapy.Spider):
    """
    自定义爬虫类，继承自scrapy.Spider类
    """
    name = "quotes"  # 名称，区分不同的spider爬虫
    allowed_domains = ["quotes.toscrape.com"]  # 允许爬取的域名
    start_urls = ["https://quotes.toscrape.com"]  # url列表

    def parse(self, response):
        """
        解析响应数据
        
        :param response: 需要解析的响应对象
        :return: 解析后的数据结果
        """
        for quote in response.css("div.quote"):
            # 获取第一页的内容  
            item = ScrapyTest01Item()
            item["title"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()
            item["tags"] = quote.css("div.tags a.tag::text").getall()
            yield item

            # 继续获取下一页的内容
            next_page = response.css("li.next a::attr(href)").get()
            if next_page:
                yield response.follow(next_page, self.parse)

