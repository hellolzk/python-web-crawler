import scrapy
import json
import csv
from douyu.pachong.items  import PachongItem
class PaSpider(scrapy.Spider):
    name = 'pa'
    allowed_domains = ['www.douyu.com']
    base_url='https://m.douyu.com/api/room/list?page={}&type=CSGO'
    offset=0
    start_urls = [base_url.format(offset)]
    #names = []  # 这三个列表记录我们获取的信息
    #roomnames = []
    #redu = []
    #friendInfo=[]
    def parse(self, response):
        data_list = json.loads(response.body)['data']
        if len(data_list['list'])==0:
            return
        for data in data_list['list']:
            item=PachongItem()
            #self.names.append(data['nickname'])
            #self.roomnames.append(data['roomName'])
            #self.redu.append(data['hn'])
            item['name']=data['nickname']
            item['rommname']=data['roomName']
            item['picture']=data['verticalSrc']
            item['redu']=data['hn']
            yield item
        self.offset +=1
        url=self.base_url.format(self.offset)
        yield scrapy.Request(url,callback=self.parse,dont_filter=True)#不自动过滤