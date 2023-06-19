from lxml import etree
import requests
import csv

fp = open('douyuLOL.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('houseName', 'houseTape',  'hostName', 'popularity'))

urls = ['https://www.douyu.com/g_LOL']
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

for url in urls:
    html = requests.get(url,headers=headers,timeout=2.0)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//li[@class="layout-Cover-item"]')# <ul class="layout-Cover-list">

    for info in infos:
        houseNames = info.xpath('div/a/div/div/h3[@class="DyListCover-intro"]/@title')[0]  # name = info.xpath('td/div/a/text()')[0].strip('\n ')

        houseTapes = info.xpath('div/a/div/div/span[@class="DyListCover-zone"]/text()')[0]

        hostNames = info.xpath('div/a/div/div/h2/div[@class="DyListCover-userName is-template"]/text()')[0]

        a = info.xpath('div/a/div/div/span[@class="DyListCover-hot is-template"]/text()')[0]
        popularitys=a.strip('万')
        popularitys=float(popularitys)
        writer.writerow([houseNames, houseTapes, hostNames, popularitys])

fp.close()

