import socket
from multiprocessing import Process

class web_server(object):
    '''   '''
    def __init__(self):
        # 建立tcp链接
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定任意ip和端口，ip和端口为元组组合
        #self.socket.bind(("", port))

    def bind(self,port):
        # 绑定任意ip和端口，ip和端口为元组组合
        self.socket.bind(('',port))

    def start(self):

        # 监听连接
        self.socket.listen(128)

        # 多进程接收客户端发送的请求
        while True:
            # 接收数据，返回值为客户端socket和地址
            client_socket, client_address = self.socket.accept()
            print("[%s,%s]已经链接上了" % client_address)
            client_handle_process = Process(target=self.handle_client, args=(client_socket,))

            # 开始进程
            client_handle_process.start()

            # client_socket已经在process中知道了，可以关闭
            client_socket.close()

    def handle_client(self,client_socket):
        """处理客户端请求"""
        # 接收客户端的数据
        request_data = client_socket.recv(1024)
        print('request_data:',request_data)
        #分离出请求的地址/index.html
        #request_lines = request_data.splitlines()
        #for i in request_lines:
            #print(i)
        # 构建需要响应回客户端的数据
        try:
            #二进制读取
            response_body  =open('D:/BaiduNetdiskDownload/资料/资料/file/part07/7.2.html','rb').read()
        except IOError:
            response_start = 'HTTP/1.1 404 Not Found\r\n'
            response_headers = 'Server:My Server\r\n'
            response_body = 'The Html Not Found'
            response = response_start + response_headers + "\r\n" + str(response_body)

        response_start = 'HTTP/1.1 200 OK\r\n'
        response_headers = 'Server:My Server\r\n'
        #response_body = 'hello world'
        response = response_start + response_headers + "\r\n" + response_body.decode('utf-8')
        #print('response:',response)

        # 向客户端返回响应数据，send需要bytes类型，需要转换为bytes
        client_socket.send(bytes(response,'utf-8'))

        # 关闭与客户端的链接
        client_socket.close()

def main():
    http = web_server()
    http.bind(8080)
    http.start()

if __name__ == "__main__":
    main()







