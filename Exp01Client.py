import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            reply = client_socket.recv(1024).decode('utf-8')
            if reply:
                print(reply)
            else:
                break
    except Exception as e:
        print("Disconnected from server",e)
        client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost',8888))
        print("Connected to server")

        name = input("Enter your name: ")
        client_socket.send(name.encode('utf-8'))

        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
        while True:
            message = input()
            if message:
                client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print("Connection Error",e)
        client_socket.close()

start_client()