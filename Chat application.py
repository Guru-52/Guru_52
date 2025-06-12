import socket
import threading

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345      # Arbitrary non-privileged port

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
import socket
import threading

SERVER_IP = '192.168.1.100'  # Change this to the server's IP
PORT = 12345

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print("\n" + message)
        except:
            print("Disconnected from server.")
            sock.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    name = input("Enter your name: ")
    client.send(f"{name} has joined the chat.".encode('utf-8'))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        if msg.lower() == 'exit':
            client.send(f"{name} has left the chat.".encode('utf-8'))
            break
        client.send(f"{name}: {msg}".encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
