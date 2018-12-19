import turtle
t = turtle.Pen()
t.reset()
for x in range(1,5):
    t.forward(50)
    t.left(90)
t.reset()

for x in range(1,9):    ##循环八次
    t.forward(100)      ##前进100像素
    t.left(225)         ##向左旋转225度
t.reset()
for x in range(1,20):
    t.forward(100)
    t.left(95)
t.reset()
for x in range(1,19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)