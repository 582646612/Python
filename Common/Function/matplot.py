#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def tiao():
    # 构建数据
    GDP = [12406.8,13908.57,9386.87,9143.64]

    # 中文乱码的处理
    plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘图
    plt.bar(range(4), GDP, align = 'center',color='steelblue', alpha = 0.8)
    # 添加轴标签
    plt.ylabel('GDP')
    # 添加标题
    plt.title('四个直辖市GDP大比拼')
    # 添加刻度标签
    plt.xticks(range(4),['北京市','上海市','天津市','重庆市'])
    # 设置Y轴的刻度范围
    plt.ylim([5000,15000])

    # 为每个条形图添加数值标签
    for x,y in enumerate(GDP):
        plt.text(x,y+100,'%s' %round(y,1),ha='center')
    plt.show()
def tiao1():
    Y2016 = [15600, 12700, 11300, 4270, 3620]
    Y2017 = [17400, 14800, 12000, 5200, 4020]
    labels = ['北京', '上海', '香港', '深圳', '广州']
    bar_width = 0.45

    # 中文乱码的处理
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘图
    plt.bar(np.arange(5), Y2016, label='2016', color='steelblue', alpha=0.8, width=bar_width)
    plt.bar(np.arange(5) + bar_width, Y2017, label='2017', color='indianred', alpha=0.8, width=bar_width)
    # 添加轴标签
    plt.xlabel('Top5城市')
    plt.ylabel('家庭数量')
    # 添加标题
    plt.title('亿万财富家庭数Top5城市分布')
    # 添加刻度标签
    plt.xticks(np.arange(5) + bar_width, labels)
    # 设置Y轴的刻度范围
    plt.ylim([2500, 19000])

    # 为每个条形图添加数值标签
    for x2016, y2016 in enumerate(Y2016):
        plt.text(x2016, y2016 + 100, '%s' % y2016)

    for x2017, y2017 in enumerate(Y2017):
        plt.text(x2017 + bar_width, y2017 + 100, '%s' % y2017)
    # 显示图例
    plt.legend()
    plt.show()
def tiao2():
    # 导入数据
    data = pd.read_excel('C:\\Users\\Administrator\\Desktop\\货运.xls')

    # 绘图
    plt.bar(np.arange(8), data.loc[0, :][1:], color='red', alpha=0.8, label='铁路', align='center')
    plt.bar(np.arange(8), data.loc[1, :][1:], bottom=data.loc[0, :][1:], color='green', alpha=0.8, label='公路',
            align='center')
    plt.bar(np.arange(8), data.loc[2, :][1:], bottom=data.loc[0, :][1:] + data.loc[1, :][1:], color='m', alpha=0.8,
            label='水运', align='center')
    plt.bar(np.arange(8), data.loc[3, :][1:], bottom=data.loc[0, :][1:] + data.loc[1, :][1:] + data.loc[2, :][1:],
            color='black', alpha=0.8, label='民航', align='center')
    # 添加轴标签
    plt.xlabel('月份')
    plt.ylabel('货物量(万吨)')
    # 添加标题
    plt.title('2017年各月份物流运输量')
    # 添加刻度标签
    plt.xticks(np.arange(8), data.columns[1:])
    # 设置Y轴的刻度范围
    plt.ylim([0, 500000])

    # 为每个条形图添加数值标签
    for x_t, y_t in enumerate(data.loc[0, :][1:]):
        plt.text(x_t, y_t / 2, '%sW' % (round(y_t / 10000, 2)), ha='center', color='white')

    for x_g, y_g in enumerate(data.loc[0, :][1:] + data.loc[1, :][1:]):
        plt.text(x_g, y_g / 2, '%sW' % (round(y_g / 10000, 2)), ha='center', color='white')

    for x_s, y_s in enumerate(data.loc[0, :][1:] + data.loc[1, :][1:] + data.loc[2, :][1:]):
        plt.text(x_s, y_s - 20000, '%sW' % (round(y_s / 10000, 2)), ha='center', color='white')

        # 显示图例
    plt.legend(loc='upper center', ncol=4)
    # 显示图形
    plt.show()
def bing():
    # 设置绘图的主题风格（不妨使用R中的ggplot分隔）
    plt.style.use('ggplot')

    # 构造数据
    edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
    labels = ['中专', '大专', '本科', '硕士', '其他']

    explode = [0, 0.1, 0, 0, 0]  # 用于突出显示大专学历人群
    colors = ['#9999ff', '#ff9999', '#7777aa', '#2442aa', '#dd5555']  # 自定义颜色

    # 中文乱码和坐标轴负号的处理
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
    plt.axes(aspect='equal')

    # 控制x轴和y轴的范围
    plt.xlim(0, 4)
    plt.ylim(0, 4)

    # 绘制饼图
    plt.pie(x=edu,  # 绘图数据
            explode=explode,  # 突出显示大专人群
            labels=labels,  # 添加教育水平标签
            colors=colors,  # 设置饼图的自定义填充色
            autopct='%.1f%%',  # 设置百分比的格式，这里保留一位小数
            pctdistance=0.8,  # 设置百分比标签与圆心的距离
            labeldistance=1.15,  # 设置教育水平标签与圆心的距离
            startangle=180,  # 设置饼图的初始角度
            radius=1.5,  # 设置饼图的半径
            counterclock=False,  # 是否逆时针，这里设置为顺时针方向
            wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
            textprops={'fontsize': 12, 'color': 'k'},  # 设置文本标签的属性值
            center=(1.8, 1.8),  # 设置饼图的原点
            frame=1)  # 是否显示饼图的图框，这里设置显示

    # 删除x轴和y轴的刻度
    plt.xticks(())
    plt.yticks(())
    # 添加图标题
    plt.title('芝麻信用失信用户教育水平分布')

    # 显示图形
    plt.show()
tiao1()