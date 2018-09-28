#coding:utf_8
def whilea():
    count = 0
    while (count < 9):
        print 'The count is:', count
        count = count + 1
    else:
       print count, " is not less than 5"
def whiledo():
    var = 1
    while var == 1:  # 该条件永远为true，循环将无限执行下去
        num = raw_input("Enter a number  :")
        print "You entered: ", num
def sushu():
    i = 2
    while (i < 100):
        j = 2
        while (j <= (i / j)):
            if not (i % j):
                break
            j = j + 1
        if (j > i / j):
            print i, " 是素数"
        i = i + 1

def passs():
    for letter in 'Python':
        if letter == 'h':
            pass
            print '这是 pass 块'
        print '当前字母 :', letter
def breaks():
    for letter in 'Python':  # 第一个实例
        if letter == 'h':
            break
        print '当前字母 :', letter
def continuss():
    for letter in 'Python':  # 第一个实例
        if letter == 'h':
            continue
        print '当前字母 :', letter
continuss()