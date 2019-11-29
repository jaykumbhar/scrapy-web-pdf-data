import scrapy
import fitz
from io import StringIO
import urllib
from ..items import PocworkItem
from datetime import datetime
class QuotesSpider(scrapy.Spider):
    name = "anthem_Account_Summary"
    start_urls = ['https://www.businesswire.com/news/home/20180531005074/en/']
    def parse(self, response):
        # urllib.request.urlretrieve('https://ir.antheminc.com/static-files/42a5e02c-6196-4246-8f50-cf466940800c', 'test.pdf')
        page = response.url.split("/")[-2]
        if 'PDF' in str(response.xpath('//body').get()):
            print("Foundd PDF>>>>>>>>>>>>>>>>>>>>.")
            filename = 'test'+str(response.url).replace('/','_').replace(':','_').replace('.','_')+'.pdf'
            self.logger.info('Saving PDF %s', filename)
            data = urllib.request.urlretrieve(response.url, filename)
        else:
            filename = 'downloadData/quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            responseexpecteddata = response.css('#bw-news-view :nth-child(1)')
            item = PocworkItem()
            # for mytext in responseexpecteddata:
                # print(mytext)
                # item['contact'] = mytext.css('.epi-fontLg , .bwalignc b ::text').get()
                # item['author'] = mytext.css('blockquote+ p , .epi-fontLg , .bwalignc b ::text').get()
            # print(item)
            item['websiteContent'] = responseexpecteddata.get()+' this is testing for diffrance check'
            item['website'] = response.url
            item['date'] = datetime.now()
            yield item 
       
# def Extractdata(pdfFile):
#     data = urllib.request.urlretrieve(pdfFile, 'test'+str(pdfFile)+'.pdf')
#     return data
    
