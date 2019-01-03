import re
import jieba.analyse
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
from PIL import Image
import numpy as  np
def make_stopdict():
    stopdict = set()
    f = open("stopwords.txt","r",encoding='utf-8')
    lines = f.readlines()
    for l in lines:
        stopdict.add(l.strip())
    f.close()
    return stopdict
def creat(file_add):
    stopdict=make_stopdict()
    with open(file_add,encoding="utf8") as f:
        tweets = f.read()
    zhongwen_pat = re.compile(r'^[\u4e00-\u9fa5a-zA-Z]+$')
    all_content = []
    f = open("weibo.txt","w")
    for t in tweets: #tweets是从数据库中取出来的待制作词云图的文本源
        cut_list = [c for c in jieba.cut(t[0]) if zhongwen_pat.search(c)]
        cut_set = set(cut_list)
        res_set = cut_set - stopdict
        res_list = list(res_set)
        all_content.extend(res_list)
        f.writelines(res_list)
    f.close()

def get_top_keywords(file): #这里的file即上一步生成的“wei bo.txt”
    top_word_lists = [] # 关键词列表，待填充
    with open(file,'r') as f:
        texts = f.read() # 读取整个文件作为一个字符串
        result = jieba.analyse.textrank(texts,topK=100,withWeight=True) #保留最高频的400个词
        for r in result:
            top_word_lists.append(r[0])
    return top_word_lists
def get_text(file):
    with open(file,'r') as f:
        texts = f.read() # 读取整个文件作为一个字符串
    mytext = " ".join(jieba.cut(texts))
    return mytext
def draw_wordcloud(txt):
    #读入一个txt文件,基于此文本知错词云图
    color_mask =np.array(Image.open("123.png")) #读取背景图片，
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码，文件名不支持中文
        font_path="simsun.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色，默认为黑，可根据需要自定义为颜色
        background_color='black',
        #词云形状，
        mask=color_mask,
        #允许最大词汇
        max_words=400,
        #最大号字体，如果不指定则为图像高度
        max_font_size=100,
        #画布宽度和高度，如果设置了msak则不会生效
        width=600,
        height = 400,
        margin = 2,
        #词语水平摆放的频率，默认为0.9.即竖直摆放的频率为0.1
        prefer_horizontal = 0.8
    )
    wc = cloud.generate(txt) #产生词云
    # wc = cloud.fit_words(txt) #跟以上是同一意思
    # wc.to_file("weibo_cloud.jpg") #保存图片
    #显示词云图片
    plt.imshow(wc, interpolation='bilinear')
    #不现实坐标轴
    plt.axis('off')
    #绘制词云
    #plt.figure(dpi = 600)
    image_colors = ImageColorGenerator(color_mask)
    plt.imshow(wc.recolor(color_func=image_colors)) #重新上色，
    plt.show()
if __name__ == '__main__':
    add="123.txt"
    creat(add)
    file = 'weibo.txt'
    dic=get_text(file)
    print(get_top_keywords(file))
    draw_wordcloud(dic)
