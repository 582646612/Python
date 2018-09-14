import socket
import re
import sys

g_documents_root = "./html"

def main():
    if len(sys.argv) == 2:
        port_str = sys.argv[1]
        if port_str.isdigit():
            port = int(port_str)
        else:
            print("请输入正确的端口号")
            return
    else:
        print("请以 python3 xxx.py 8888 方式运行服务器")
        return

    """整体的流程控制"""
    # 创建tcp的套接字
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定信息
    server_socket.bind(("",8888))
    # 监听变为被动的套接字
    server_socket.listen(250)
    while True:
        # accpet
        new_socket, new_add = server_socket.accept()
        # 接受数据
        recv_data = new_socket.recv(2048)
        # 判断是否有数据 然后进行解码
        if not recv_data:
            new_socket.close()
            continue
        request = recv_data.decode()
        # print(request)
        request_lines = request.splitlines()
        for i, line in enumerate(request_lines):
            print(i, line)
        # 正则表达式 解析发送过来的请求
        #  GET / HTTP/1.1
        # GET /index.html HTTP/1.1
        # POST /xxx.html
        # GET /home/show_goods.html
        # GET /home/logo.png
        #[^ ]
        ret = re.match(r"([^/]*)([^ ]*)", request_lines[0])
        file_path = ret.group(2)
        if file_path == "/":
            file_path = "/index.html"
        print("++++++++++++++++文件的路径:",file_path)
        # 找到对应的文件 打开文件读取数据 返回给客户端
        try:
            f = open(g_documents_root + file_path,"rb")
        except Exception as ret:
            print("打开文件失败:",ret)
            # 404
            response_header = "HTTP/1.1 404 Not Found\r\n"
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "\r\n"

            response_body = "sorry,没有你要的文件"
            response = response_header + response_body
            new_socket.send(response.encode())
            # close
            # new_socket.close()

        else:
            content = f.read()

            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "\r\n"
            response_body = content

            new_socket.send(response_header.encode())
            new_socket.send(response_body)
            # new_socket.close()
        finally:
            new_socket.close()


if __name__ == '__main__':
    main()