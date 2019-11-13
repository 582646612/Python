import execjs #PyExecJS
def get_des_psswd(date):
    jsstr = get_js()
    ctx = execjs.compile(jsstr) #加载JS文件
    return  ctx.call('hex_md5',date)#调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数
def get_js():
    f = open("md5.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr

if __name__ == '__main__':
    print(get_des_psswd('123'))