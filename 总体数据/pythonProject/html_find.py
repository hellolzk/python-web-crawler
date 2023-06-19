import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


headers={
    'cookie': 'dy_did=efd1e32d2c2595f6a8cffd1500011601; dy_auth=679cy26%2B%2Bm8UhMpq9Z%2BEODwTxN7G5VQtVluDOIGq9tSHI5Q6jVRWotcffiAKc5g%2FT8LDBlob4wVXJQ%2BAn%2FgiryMY0WIZOKtTLI1%2BVrJhfu9x%2FUM1PNjhzaI; wan_auth37wan=ccfb9c77df27ekkfuEP1hAn1%2FNq%2Ffx86hR1PRc2lKBNcY2j%2BdRxeXBH12lquV0tdrlZVzrzq%2FLdciKQ4tpayhGQBakRQKQec9Um7Ja3fgks4dtij2R4; loginrefer=pt_05bilhiin6fk5; msg_auth=ea4d5e163d8837d34ded8e8bbd257a3af504d192; msg_uid=lWAop2Pm0K7v; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1653134845,1653529932,1653590422; post-csrfToken=io2edlzvqc; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1653591041',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url='https://www.douyu.com/directory/all' #url是目标的网址：斗鱼直播排行主页
list=[]
#循环外先定义几个数据
coclums=['房间名','主播名','类型','标签','热度']
response = requests.get(url, headers=headers)#获取目标网页返回的内容
html = response.text


html_tree = bs(html, 'html.parser')#html.parser是bs4的html解析器。
host_infos = html_tree.find("div", {"class": "layout-Module-container layout-Cover ListContent"})
host_list = host_infos.find_all("li")
for i in host_list:
    home_name = i.find("h3").get_text()
    home_name1 = i.find("div", {"class": "DyListCover-userName"}).get_text()
    home_type = i.find("span", {"class": "DyListCover-zone"}).get_text()
    home_tag = i.find("span", {"class": "HeaderCell-label-wrap is-od"})
    home_num = i.find("span", {"class": "DyListCover-hot"}).get_text()
    #将每一项数据都加入到我们列表中
    list.append([home_name, home_name1, home_type, home_tag, home_num])
    #接下来我们将数据整合，用前面定义的列名columns，用dataframe变成二维的，便于我们查看
    df = pd.DataFrame(list, columns=coclums)
    df.to_excel("hot-100.xlsx",index=False)
