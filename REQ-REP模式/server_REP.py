# REQ-REP模式
# Python端 --> Server端(使用python进行模拟)
# 这是一个示例 Socket Server Python 脚本。
import time
import zmq
import json
def server():
    context = zmq.Context()
    # 当前模式为REP-REQ模式，需要依赖 客户端(client) 唤醒。
    # 服务端为REP对象
    socket = context.socket(zmq.REP)
    # 绑定的tcp通信端口为：55555
    socket.bind("tcp://*:55556")

    try:
        while True:
            try:
                """
                在该模式下，Python需要等待Unity主动调用，才能进行响应。
                """
                print("等待接受消息...")
                # 将 socket 接收到的消息按照“utf-8”格式进行编码，保存到message里
                message = socket.recv().decode('utf-8')
                print(f"Received request: {message}")

                # 设置循环退出出口，可以自行决定是否保留
                if message == "EXIT":
                    print("收到退出请求")
                    break

                # 避免接收过于频繁
                time.sleep(1)
                """
                    获得需要发送的消息的代码逻辑
                """

                message_dict = {
                    "python_exe": 'process_name',
                    "function": 'process_function_name',
                    "Param": {
                        "Content": "This is the Response from Python!"
                    }
                }

                reply = json.dumps(message_dict, indent=2)
                socket.send_string(reply)
            except zmq.Again:
                # 捕获 zmq.Again 异常，如果没有消息就继续循环
                time.sleep(0.1)  # 等待一小段时间再检查
    finally:
        socket.close()
        context.term()
        print("套接字已关闭")

if __name__ == '__main__':
    server()