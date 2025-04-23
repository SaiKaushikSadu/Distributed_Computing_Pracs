import socket
import threading

clients = {}
lock = threading.Lock()

def handle_client(client_socket, client_address):
    try:
        name = client_socket.recv(1024).decode('utf-8')
        with lock:
            clients[client_socket] = name
        print(f"New client connected: {client_address} as {name}")
        broadcast(f"{name} has joined the chat",client_socket)
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"{name}: {message}")
                broadcast(f"{name}: {message}",client_socket)
            else:
                break
    finally:
        remove_client(client_socket)

def broadcast(message, client_socket):
    with lock:
        for client in clients:
            if client != client_socket:
                try:
                    client.sendall(message.encode('utf-8'))
                except:
                    remove_client(client)

def remove_client(client_socket):
    with lock:
        name = clients.get(client_socket,'Unknown')
        print(f"{name} Disconnected ")
        broadcast(f"{name} has left the chat",client_socket)
        if client_socket in clients:
            del clients[client_socket]
        client_socket.close()

def start_server():
    # Configure socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('localhost',8888))
    server_socket.listen()
    print('Group chat server is running on port 8888')
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client,args=(client_socket,client_address)).start()

start_server()