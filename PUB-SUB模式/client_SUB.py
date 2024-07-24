# 基于PUB-SUB模式
# Unity 端 --> client端 (为方便测试，此处使用Python代码进行模拟)
import time
import zmq
import json

def client():
    context = zmq.Context()
    # 创建一个REQ类型的socket
    socket = context.socket(zmq.SUB)
    # 连接到服务器的tcp通信端口
    socket.connect("tcp://localhost:55557")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")  # 订阅所有消息

    while True:
        print("正在等待接收消息...")
        response = socket.recv().decode('utf-8')
        response_dict = json.loads(response)
        content = response_dict['Param']['Content']
        print(f"Received reply: {content}")

        time.sleep(1)  # 接收间隔时间

if __name__ == '__main__':
    client()
"""
PUB-SUB模式，Unity端只需要负责接收消息，不需要反馈。
"""