#coding=utf-8
import jieba
from PIL import Image
import numpy as  np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
bg=np.array(Image.open("123.png"))
text_path="weibo.txt"
with open(text_path) as f:#,encoding="utf8"
     mytext = f.read()
mytext = " ".join(jieba.cut(mytext))
wordcloud = WordCloud(font_path="simsun.ttf",background_color="white",max_words=2000,
                mask=bg, max_font_size=60,random_state=102,scale=8,).generate(mytext)
# print(mytext)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()