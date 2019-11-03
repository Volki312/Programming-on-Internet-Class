import socket
import _thread

messageCache = " "

def start_server():
    IP = '127.0.0.1'
    PORT = 50200
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen()
    return s

def connect_to_next_node():
    print("Press ENTER when ready...")
    input()
    nn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nn.connect(('127.0.0.1', 50000))
    return nn

def send_messages(nn):
    global messageCache
    while True:
        messageCache = input("Enter a message: ")
        nn.sendall(str.encode(messageCache))

def pass_messages(pn, nn):
    global messageCache
    while True:
        recievedMessage = pn.recv(1024).decode()
        if recievedMessage == messageCache:
            print("Old message recieved, node closed")
        else:
            print(recievedMessage)
            nn.sendall(str.encode(recievedMessage))

s = start_server()
nn = connect_to_next_node()
_thread.start_new_thread(send_messages,(nn, ))

while True:
    pn, adr = s.accept()
    pass_messages(pn, nn)