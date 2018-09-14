from socket import *
import threading
import getpass
import uuid
import os
import multiprocessing

# 创建socket对象(udp)
My = socket(AF_INET, SOCK_DGRAM)
# 广播通知（通知局域网内所有用户）
My.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# udp绑定端口
port = 2214
# udp协议绑定端口
My.bind(('', port))
# 创建socket对象（tcp）
sock_server = socket(AF_INET, SOCK_STREAM)
# tcp协议绑定端口
port1 = 2213
# tcp协议绑定端口
sock_server.bind(('', port1))
# 监听
sock_server.listen(250)

# 广播ip
ip = '192.168.17.255'
# 地址广播ip， 端口
add = (ip, port)
# 获取用户名
name = getpass.getuser()
# uuid为该程序生成唯一识别码
uuid = str(uuid.uuid1())
# 创建字典保存用户要发送的信息
directory = {'name': name, 'uuid': uuid}
# 创建列表保存返回在线用户数据
user_list = []
# 发送文件的目标ip
des_ip = ''
# 发送文件的路径
file = ''


def online():  # 定义上线的函数
    directory['state'] = 'online'  # 字典增加状态的键值对，上线状态为online


def offline():  # 定义下线的函数
    directory['state'] = 'offline'  # 字典增加状态的键值对， 下线的状态为offline


def send_back():  # 定义回应函数
    directory['state'] = 'i am online too'  # 字典增加状态键值对


def send_msg():  # 定义发送用户信息的函数
    str_directory = str(directory).encode('utf-8')  # 把字典转化为字符串类型，转码成二进制数据后赋值给变量str_directory
    My.sendto(str_directory, add)  # 根据add内的ip和端口发送字典生成的二进制数据给局域网内的用户


def rev_msg():  # 定义接收用户信息的函数
    ges, res = My.recvfrom(8180)  # 用户接收的最大数据为9999个字节,ges为接收到的字典转化的二进制数据，res为对方的ip和端口
    rev = eval(ges.decode())  # ges为二进制数据，先解码为字符串后通过eval函数重新转化为字典，用变量rev保存字典
    return rev, res  # 用元祖保存返回的数据rev，res


def send_content(sock, co):  # 防止缓冲区内存不够
    send_len = 0  # 发送的长度开始为０
    while True:  # 循环发送直到把读取到的内容发送完成
        data = sock.send(co[send_len:])  # 对读取到的内容一点点进行发送,发送到哪里，下次从切片处继续发送
        send_len += data  # 发送总长度每次加上发送的data长度
        if send_len == len(co):  # 当发送的长度等于读取到的长度时，读取到的部分已经发送完成，继续读取，继续发送，直到读取完成
            break


def send_file():
    # 创建socket对象（tcp）
    sock = socket(AF_INET, SOCK_STREAM)
    # 连接服务器
    sock.connect((des_ip, port1))
    if os.path.isfile(file) is True:
        sen_f(sock, file)
        send_content(sock, 'q'.encode())
        print('文件发送完成')
    elif os.path.isdir(file) is True:
        folder_di(sock, file)
        send_content(sock, 'q'.encode())
        print('文件夹发送完成')


def sen_f(sock, new):
    send_content(sock, 'f'.encode())
    file_name = os.path.basename(new)  # file_name是文件名称
    file_name_en = file_name.encode('utf-8')  # file_name进行编码
    file_name_len = len(file_name_en)  # file_name长度
    file_name_len_str = '%08d' % file_name_len  # 文件长度转化为8位数，不足8位数用0补足
    file_name_enc = file_name_len_str.encode()
    send_content(sock, file_name_enc)  # 发送文件名长度
    # 发送文件名
    send_content(sock, file_name_en)
    # 发送文件内容长度
    content_len = os.path.getsize(new)  # 对获取到的文件内容长度进行编码赋值给content_len
    content_len_str = '%08d' % content_len  # 文件长度转化为字符串，补足8位
    content_len_en = content_len_str.encode()  # 文件内容长度转化为二进制编码
    send_content(sock, content_len_en)  # 发送文件内容长度
    # 发送文件内容
    f = open(new, 'rb')  # 只读模式打开文件
    while True:
        content = f.read(1024)  # 读取文件内容长度1024字节
        if not content:
            print('文件%s发送成功' % file_name)
            break
        else:
            send_content(sock, content)  # 对读取到的文件内容进行发送
    f.close()
    # ck.close()     ！！！！！！！！！！！！sock这里不能关闭


def send_folder(sock, s):
    send_content(sock, 'd'.encode())
    folder_name = os.path.basename(s)  # new_file为新的文件夹路径，folder_name为文件夹的名字
    folder_name_en = folder_name.encode()  # 对文件夹的名字进行编码
    folder_name_len = len(folder_name_en)  # 计算文件夹名字编码的长度
    folder_name_len_str = '%08d' % folder_name_len  # 文件夹的编码长度转化为字符串
    folder_name_len_en = folder_name_len_str.encode()  # 文件夹的长度进行编码
    # 发送文件夹名字的长度
    send_content(sock, folder_name_len_en)
    # 发送文件夹的名字
    send_content(sock, folder_name_en)
    print('文件夹%s发送完成' % folder_name)


def folder_di(sock, n):

    send_folder(sock, n)
    for i_name in os.listdir(n):
        new_file = n + '/' + i_name
        if os.path.isdir(new_file):
            folder_di(sock, new_file)

        elif os.path.isfile(new_file):
            sen_f(sock, new_file)
    send_content(sock, 'c'.encode())


def rev_file(long):  # 接受发送的tcp数据
    z = b''  # 定义一个空字节
    x = 0  # 接收到的长度为0
    while True:
        v = sock_new.recv(long - x)  # 接收tcp数据（最大数据）
        z += v  # 接受的内容自加
        x += len(v)  # 接收到的长度自加
        if x == long:  # 如果接收到的长度等于需要接收到的长度
            break  # 退出循环
    return z.decode()  # 函数返回解码后的接收数据


def res_file():
    pp = '/home/zhong/桌面'
    os.chdir(pp)
    nn = os.listdir('.')
    if cc in nn:
        print('该文件名称已存在')
    else:
        while True:
            a = rev_file(1)
            if a == 'f':
                n = rev_file(8)  # 文件名长度发送时定义长度为8
                m = int(n)  # 字符串型转化为数值型
                print('文件名长度为：%s' % m)  # 打印文件名长度
                l = rev_file(m)  # 知道文件名长度后，接受文件名
                print('文件名称为：%s' % l)  # 打印文件名称
                q = rev_file(8)  # 文件内容长度发送时定义长度为8，接受文件内容长度
                w = int(q)  # 字符串转化为数值型
                print('文件内容长度为：%s' % w)  # 打印文件内容长度
                # 接受文件内容
                r = open(l, 'w')
                jj = rev_file(w)
                r.write(jj)
                r.close()

                # sock_new.close()
                print('文件%s接收完成' % l)
            elif a == 'd':
                uy = rev_file(8)
                tr = int(uy)

                print('文件夹名长度为：%s' % tr)
                kj = rev_file(tr)
                print('文件夹名为：%s' % kj)
                os.mkdir(kj)
                os.chdir(kj)
                print('文件夹%s接收完成' % kj)
            elif a == 'c':
                os.chdir('..')
            elif a == 'q':
                break


def rev_wen():
    while True:
        global sock_new
        sock_new, address = sock_server.accept()
        t10 = multiprocessing.Process(target=res_file)
        t10.start()


def fun():
    while True:  # 接收信息为上线后死循环接受
        rev, res = rev_msg()  # 调用接收信息函数
        if rev['uuid'] == uuid:  # 当接收到的uuid等于自己的uuid时，不打印
            continue
        else:
            h = [x for x in rev.keys()]
            if 'msg' in h:
                print('%s ,%s' % (rev['msg'], res[0]))
                if '是否接收' in rev['msg']:
                    aa = rev['msg']
                    bb = aa.split('：')
                    rr = bb[1].split('\n')
                    global cc
                    cc = rr[0]
                elif rev['msg'] == '接收文件':
                    t4 = threading.Thread(target=send_file)
                    t4.start()
            else:
                if rev['state'] == 'online' and b is True:
                    print('%s, %s, %s, %s' % (res[0], rev['name'], rev['uuid'], rev['state']))
                    rev['ip'] = res[0]
                    user_list.append(rev)
                    send_back()
                    str_directory = str(directory).encode('utf-8')  # 把字典转化为字符串类型，转码成二进制数据后赋值给变量str_directory
                    My.sendto(str_directory, (res[0], port))
                elif rev['state'] == 'offline' and b is True:
                    print('%s, %s, %s, %s' % (res[0], rev['name'], rev['uuid'], rev['state']))
                    for i in range(len(user_list)):
                        if user_list[i]['uuid'] == rev['uuid']:
                            del user_list[i]
                elif rev['state'] == 'i am online too' and b is True:
                    rev['ip'] = res[0]
                    user_list.append(rev)
                    print('%s, %s, %s, %s' % (res[0], rev['name'], rev['uuid'], rev['state']))


b = False


def main():
    global b
    while True:
        str_a = input('请输入指令（1登陆,2下线,3打印用户列表,4发送信息给目标用户,5发送文件或目录,6是否接受文件,0,退出程序）:')
        if str_a.isdigit() is True:
            a = int(str_a)
            if a == 1 and b is False:
                b = True
                online()
                send_msg()

                t = threading.Thread(target=fun)
                t.start()
            elif a == 1 and b is True:
                print('你已经登陆了')
            elif a == 3 and b is True:
                print(user_list)
            elif a == 3 and b is False:
                print('你还没登陆，无法打印用户列表')
            elif a == 4 and b is True:
                if len(user_list) == 0:
                    print('还没有用户登陆，无法发送消息')
                else:
                    d = input('请输入对方ip：')
                    i = 0
                    while i < len(user_list):
                        if user_list[i]['ip'] == d:
                            c = input('请输入要发送的信息：')
                            directory['msg'] = c
                            e = str(directory).encode('utf-8')
                            My.sendto(e, (d, port))
                        elif user_list[i]['ip'] != d and i == len(user_list) - 1:
                            print('你输入的ip不存在或不在线')
                        i += 1
            elif a == 4 and b is False:
                print('你还没登陆，无法发送消息')
            elif a == 5 and b is True:
                if len(user_list) == 0:
                    print('还没有用户登陆，无法发送文件')
                else:
                    global des_ip
                    des_ip = input('请输入对方ip：')
                    j = 0
                    while j < len(user_list):
                        if user_list[j]['ip'] == des_ip:
                            global file
                            file = input('请输入要传送的文件路径（绝对路径）：')
                            if os.path.exists(file) is True:
                                bas_name = os.path.basename(file)
                                if os.path.isdir(file):
                                    directory['msg'] = '我要给你发送文件夹：' + bas_name + '\n' + '是否接收?'
                                    e = str(directory).encode('utf-8')
                                    My.sendto(e, (des_ip, port))
                                elif os.path.isfile(file):
                                    directory['msg'] = '我要给你发送文件：' + bas_name + '\n' + '是否接收?'
                                    e = str(directory).encode('utf-8')
                                    My.sendto(e, (des_ip, port))
                            else:
                                print('你输入的路径不存在')
                                break
                        elif user_list[j]['ip'] != des_ip and j == len(user_list) - 1:
                            print('你输入的ip不存在或不在线')
                        j += 1
            elif a == 5 and b is False:
                print('你还没有上线，无法发送文件')
            elif a == 6 and b is True:
                p = input('请输入对方ip:')
                t = 0
                while t < len(user_list):
                    if user_list[t]['ip'] == p:
                        o = input('yes/no?:')
                        if o == 'yes':
                            t3 = multiprocessing.Process(target=rev_wen)
                            t3.start()
                            directory['msg'] = '接收文件'
                            e = str(directory).encode('utf-8')
                            My.sendto(e, (p, port))
                        elif o == 'no':
                            directory['msg'] == '不接收文件'
                            e = str(directory).encode('utf-8')
                            My.sendto(e, (p, port))
                        else:
                            print('命令错误,请输入yes或no')
                    elif user_list[t]['ip'] != p and t == len(user_list) - 1:
                        print('你输入的ip不存在或者不在线')
                    t += 1
            elif a == 6 and b is False:
                print('你还没上线,无法接收文件')

            elif a == 2 and b is True:
                b = False
                offline()
                send_msg()
                for i in range(len(user_list)):
                    del user_list[i]
            elif a == 2 and b is False:
                print('你还没登陆，无法下线')
            elif a == 0:
                break
            else:
                print('请输入0至６的整数')

        else:
            print('请输入数字')


if __name__ == '__main__':  # 测试
    main()