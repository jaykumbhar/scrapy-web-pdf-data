import scrapy
import fitz
import urllib
from ..items import PocworkItem
from datetime import datetime
import requests, PyPDF2, io
import os
class QuotesSpider(scrapy.Spider):
    name = "anthem_Account_Summary"
    start_urls = [
        'https://www.businesswire.com/news/home/20180531005074/en/',
        'https://www.businesswire.com/portal/site/home/',
        'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
        'https://ir.antheminc.com/static-files/99d2cb18-290c-4568-9252-01e9b27a740a',
    ]
    def parse(self, response):
        # urllib.request.urlretrieve('https://ir.antheminc.com/static-files/42a5e02c-6196-4246-8f50-cf466940800c', 'test.pdf')
        page = response.url.split("/")[-2]
        if 'PDF' in str(response.xpath('//body //*[not(self::script)]/text()').get()):
            print("Foundd PDF>>>>>>>>>>>>>>>>>>>>.")
            data = []
            i = 0
            myfile = requests.get(response.url,allow_redirects=True)
            open('hello.pdf', 'wb').write(myfile.content)
            pdfpath = os.path.abspath("hello.pdf")
            doc = fitz.open(pdfpath)
            while i < doc.pageCount:
                page1 = doc.loadPage(i)
                page1text = page1.getText()
                data.append(str(page1text))
                i += 1
            responseexpecteddata = ''.join([str(elem) for elem in data]) 
            item = PocworkItem()
            item['websiteContent'] = str(responseexpecteddata)+'this is testing for diffrance check'
            item['website'] = response.url
            item['date'] = datetime.now()
            yield item 
        else:
            # filename = 'downloadData/quotes-%s.html' % page
            # with open(filename, 'wb') as f:
            #     f.write(response.body)
            # responseexpecteddata = response.css('#bw-news-view :nth-child(1)').get()
            # responseexpecteddata = response.css('body::*[not(self::script)]/text()').get()
            responseexpecteddata = response.css('body').get()#//body//p//text()
            item = PocworkItem()
            item['websiteContent'] = responseexpecteddata.replace('</body>',' this is testing for diffrance check </body>')
            item['website'] = response.url
            item['date'] = datetime.now()
            yield item 