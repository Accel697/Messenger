import socket
import threading

host = '127.0.0.1'
port = 12345

def receiveMessage(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break

def sendMessage(sock):
    while True:
        message = input()
        sock.send(message.encode('utf-8'))

def startClient():
    client = socket.socket()
    client.connect((host, port))

    name = input("Введите ваше имя: ")
    client.send(name.encode('utf-8'))


    threadReceive = threading.Thread(target=receiveMessage, args=(client,))
    threadReceive.start()

    threadSend = threading.Thread(target=sendMessage, args=(client,))
    threadSend.start()

startClient()