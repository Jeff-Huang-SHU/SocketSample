# REQ-REP模式
# Unity端 --> Client端(使用python进行模拟)
# 这是一个示例 Socket Client Python 脚本。
import time
import zmq
import json

def client():
    context = zmq.Context()
    # 创建一个REQ类型的socket
    socket = context.socket(zmq.REQ)
    # 连接到服务器的tcp通信端口
    socket.connect("tcp://localhost:55556")
    try:
        while True:
            # 将消息按照“utf-8”格式进行编码并发送
            message = "This is a Request from Unity"
            socket.send_string(message)

            # 等待接收服务器的响应消息
            response = socket.recv().decode('utf-8')
            # 解析json格式
            response_dict = json.loads(response)
            content =response_dict['Param']['Content']
            print(f"Received reply: {content}")

            # 避免发送过于频繁
            time.sleep(1)
    finally:
        # 自动发送“EXIT”消息
        try:
            socket.send_string("EXIT")
            print("自动发送退出请求")
        except Exception as e:
            print(f"发送退出请求时出错: {e}")

        socket.close()
        context.term()
        print("客户端已关闭")

if __name__ == '__main__':
    client()
