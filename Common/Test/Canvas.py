from tkinter import *
def cicle():
    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3
    mainloop()
def zhixian():
    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()

def fangxing():
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=400, height=400, bg='yellow')
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()
def tuoyuna():
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()
if __name__ == '__main__':
    tuoyuna()