import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud

def trans_ch(txt):
  words = jieba.lcut(txt)
  newtxt = ''.join(words)
  return newtxt
f = open('wordCloud.text','r',encoding = 'utf-8')
txt = f.read()
f.close
txt = trans_ch(txt)
mask = np.array(Image.open("word.png"))
wordcloud = WordCloud(background_color="white",\
                      width = 800,\
                      height = 600,\
                      max_words = 200,\
                      max_font_size = 80,\
                      mask = mask,\
                      contour_width = 4,\
                      contour_color = 'steelblue',\
                        font_path =  "AaJingHongNanDiMengZhongZhong-2.ttf"
                      ).generate(txt)
wordcloud.to_file('douyuLOL_词云图.png')

