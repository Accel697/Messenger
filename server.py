import socket
import threading

host = '127.0.0.1'
port = 12345

clients = []


def handleClient(conn, addr):
    print(f"Подключен к {addr}")
    name = conn.recv(1024).decode('utf-8')
    broadcast(f"{name} присоединился к чату", conn)
    clients.append(conn)

    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if message:
                broadcast(f"{name}: {message}", conn)
            else:
                break
        except:
            break

    print(f"Отключен {addr}")
    broadcast(f"{name} покинул чат", conn)
    clients.remove(conn)
    conn.close

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message.encode('utf-8'))

def startServer():
    server = socket.socket()
    server.bind((host, port))
    server.listen()

    print(f"Сервер запущен на {host}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()

startServer()