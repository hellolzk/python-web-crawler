import numpy as np
from wordcloud import WordCloud, ImageColorGenerator  # , STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import jieba  # cutting Chinese sentences into words

#词云怎么看
def plt_imshow(x, ax=None, show=True):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(x)
    ax.axis("off")
    if show: plt.show()
    return ax

#2.3 统计词频:
#输入一个词语列表,
#输出保存每个词语出现频率的字典.
def count_frequencies(word_list):
    freq = dict()
    for w in word_list:
        if w not in freq.keys():
            freq[w] = 1
        else:
            freq[w] += 1
    return freq


if __name__ == '__main__':
    # setting paths
    fname_text = 'texts/article.txt'
    fname_stop = 'stopwords/hit_stopwords.txt'
    fname_mask = 'pictures/owl.jpeg'
    fname_font = 'SourceHanSerifK-Light.otf'

    #2.1 读取文本
    # #read in texts (an article)
    # Chinese stop words
    text = open(fname_text, encoding='utf8').read()
    STOPWORDS_CH = open(fname_stop, encoding='utf8').read().split()
    # 命令打开一个文件, 且 encoding='utf8' 告诉计算机该文件的编码方式是 ‘utf-8’, 如果没有这个设定, 会导致中文字符乱码.
    # 对打开的文件, .read() 操作会返回一个字符串. 因此代码中的 text 是字符串类型.
    # .split() 操作将字符串 (按照空格, tab\t, 换行符 \n) 分割成了一系列字符串, 因此STOPWORDS_CH 是一个由字符串组成的列表 list.

    #2.2 分词和过滤
    # processing texts: cutting words, removing stop-words and single-charactors
    word_list = [
        w for w in jieba.cut(text)
        if w not in set(STOPWORDS_CH) and len(w) > 1
    ]
    #首先用 jieba.cut(text) 函数将字符串 text 分割成一个个词或词组 (该函数返回的是一个’生成器 generator),
    #然后对里面的每一个词, 过滤掉没有意义的 ‘停用词’ (w not in STOPWORDS_CH), 最后只保留长度大于1的词组 (len(w) > 1).

    #2.3 统计词频（调用函数）
    freq = count_frequencies(word_list)

    #3.3 从图片提取颜色
    #首先读取图片, 将其转化为 RGB 数组;
    #然后用 ImageColorGenerator 从中提取颜色, 它会得到一个颜色生成器, 依照每个词所占的矩形区域的颜色平均来确定改词最终的颜色.
    # processing image
    im_mask = np.array(Image.open(fname_mask))
    im_colors = ImageColorGenerator(im_mask)

    #3.2 设置背景颜色 3.3之后要修改这段代码
    #通过修改参数 background_color 来设置背景颜色, 比如把背景改成白色:
    # generate word cloud
    wcd = WordCloud(font_path=fname_font,  # font for Chinese charactors
                    background_color='white',
                    mode="RGBA",
                    mask=im_mask,
                    )
    #3.1默认颜色
    #首先用WordCloud()建立一个词云的对象, 并设置好初始参数(字体的路径).然后基于刚刚建立的词频生成词云.
    # wcd.generate(text) # for English words
    wcd.generate_from_frequencies(freq)
    wcd.recolor(color_func=im_colors)

    #可视化&保存图片:
    ax = plt_imshow(wcd, )
    ax.figure.savefig(f'single_wcd.png', bbox_inches='tight', dpi=150)
    #拼图&保存图片:
    fig, axs = plt.subplots(1, 2)
    plt_imshow(im_mask, axs[0], show=False)
    plt_imshow(wcd, axs[1])
    fig.savefig(f'conbined_wcd.png', bbox_inches='tight', dpi=150)

