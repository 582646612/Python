import turtle as tt
# tt.TurtleScreen._RUNNING = True  # 启动绘图，在IDE中运行加这句可避免报错
# cnt = 0
# while cnt < 5:
#     tt.forward(200)
#     tt.right(144)
#     cnt += 1
# tt.done()  # 结束绘图，这将不会关闭窗口
from random import randint
tt.TurtleScreen._RUNNING = True
tt.speed(0)  # 绘图速度为最快
tt.bgcolor("black")  # 背景色为黑色
tt.setpos(-25, 25)  # 改变初始位置，这可以让图案居中
tt.colormode(255)  # 颜色模式为真彩色
cnt = 0
while cnt < 500:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tt.pencolor(r, g, b)  # 画笔颜色每次随机
    tt.forward(50 + cnt)
    tt.right(91)
    cnt += 1
tt.done()
