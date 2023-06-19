import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot

cs_16=pd.read_excel('5.28 22.xlsx')

print(cs_16['name'])

bar=(
    Bar(init_opts=opts.InitOpts(width='720px',height='320px')) #初始化柱状图
    .add_xaxis(xaxis_data=cs_16['name'].tolist()) #x轴数据写入
    .add_yaxis('2022.5.28 22点 CS：GO区 热度前30 单位：万',cs_16['hot'].tolist()) #y轴数据写入
    .set_global_opts( xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45,font_size=5))) #字体大小与倾斜程度设置
    .set_series_opts(label_opts=opts.LabelOpts(distance=10,font_size=10,rotate=30))
)

make_snapshot(snapshot, bar.render(), "5.28 22.png") #png图片生成

#https://blog.csdn.net/GODXML/article/details/120309639
