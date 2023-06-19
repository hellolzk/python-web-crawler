import json
import requests
import csv

class DouyuSpider:
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla\/5.0 (Windows NT 10.0; Win64; x64) App'
                         'leWebKit\/537.36 (KHTML, like Gecko) Chrome\/101.0.4951.67 Safari\/537.36',
        }
        self.start_url = 'https://www.douyu.com/gapi/rkc/directory/mixList/2_33/{:d}'

    def fetch_one_page(self, offset):
        """ 发起请求，获取响应数据
        :param offset: 页面序号
        :return response.content: 二进制响应体数据
        """
        response = requests.get(self.start_url.format(offset),headers=self.headers)
        return response.content

    def parse_json(self, content):
        results = json.loads(content.decode())['data']
        items = []#列表形式存储爬取信息，列表里面是元组
        num = 0
        for result in results['rl']:
            item = {}
            item['topic'] = result['c2name']
            item['title'] = result['rn']
            if result['authInfo']['desc'] =='':
                item['desc']='无'
            else:
                item['desc']=result['authInfo']['desc']
            ol = result['ol'] / 10000
            if ol == 0:
                item['hot'] = '0.0'
            else:
                item['hot'] = f'{ol:.1f}'
            item['user'] = result['nn']
            item['room_url'] = 'https://www.douyu.com/{}'.format(result['url'])
            items.append(item)
            num += 1
            print(f'完成第{num}条数据')
            print(item)
        return items, int(results['pgcnt'])

    def save_content(self, items):
        with open("5月30日./斗鱼直播5.30 下午 CF.csv", "a+",encoding="utf-8",newline='') as file:
            for data in items:
                writer = csv.writer(file)
                writer.writerow(data.values())

    def is_next(self, max_pages, offset):
        if offset <  max_pages:
            next_flag = True
        if offset >= max_pages:
            next_flag = False
        return next_flag

    def run(self):
        offset = 0
        next_flag = True
        with open("5月30日./斗鱼直播5.30 下午 CF.csv", "a+",encoding="utf-8",newline='') as file:
            data=['游戏名','房间名','主播头衔','热度/万','主播昵称','直播网址']
            writer = csv.writer(file)
            writer.writerow(data)
        while next_flag:
            offset += 1
            html = self.fetch_one_page(offset)
            items, max_pages = self.parse_json(html)
            self.save_content(items)
            print('*'*10 + f'完成第{offset}页' + '*'*10)
            print(f'最大页数{max_pages}')
            next_flag = self.is_next(max_pages, offset)
        print('已爬取所有页面')

dou_spider = DouyuSpider()
dou_spider.run()
