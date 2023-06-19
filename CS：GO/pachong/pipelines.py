# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
import csv,codecs
from scrapy.pipelines.images import ImagesPipeline
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import  CsvItemExporter
store_file = os.path.dirname(__file__) + '/spiders/ceshi.csv' #打开文件，并设置编码
file = codecs.open(filename= store_file, mode= 'wb', encoding='utf-8')# 写入csv
data=['主播名称','房间名称','网址','热度']
writer = csv.writer(file)
writer.writerow(data)

class PachongPipeline(object):
    def process_item(self, item,info):
        line = (item['name'], item['roomname'], item['picture'], item['redu'])#逐行写入
        print(item)
        writer.writerow(line)
        return item

    def close_spider(self, spider):
        file.close()

