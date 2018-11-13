def count():
    fs=[]
    def f(n):
        def s():
            return  n*n
        return s
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())