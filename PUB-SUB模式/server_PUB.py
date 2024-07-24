# 基于PUB-SUB模式
# Python 端 --> server端
import time
import zmq
import json

def server(result):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:55557")
    time.sleep(1)  # 等待订阅者连接

    message_dict = {
        "python_exe": 'process_name',
        "function": 'process_function_name',
        "Param": {
            "Content": result
        }
    }
    reply = json.dumps(message_dict, indent=2)
    socket.send_string(reply)
    print("已经成功发送!")


if __name__ == '__main__':
    while True:
        server("This is a message from Python")
        time.sleep(1)  # 发送间隔时间
"""
PUB-SUB模式，Python只需要负责发送消息，不需要接收消息，所以可以自行控制发送。
"""