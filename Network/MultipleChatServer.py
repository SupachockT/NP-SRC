from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Lock
from time import ctime

BUFFER_SIZE = 4096

class ChatLog:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_message(self, message_id):
        if not self.messages:
            return "No messages yet!"
        elif message_id == 0:
            return '\n'.join(self.messages)
        elif 0 < message_id <= len(self.messages):
            return self.messages[message_id - 1]
        else:
            return "Invalid message ID"

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.log = ChatLog()
        self.lock = Lock()

    def broadcast(self, message, client):
        for sock in self.clients:
            if sock != self.server and sock != client:
                try:
                    sock.send(message.encode())
                except:
                    print(f'{client} is offine.')
                    self.remove_client(sock)

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            client.close()

    def handle_client(self, client, address):
        client.send(b'Welcome to the chat room! Please Enter your name.\n')
        name = client.recv(BUFFER_SIZE).decode()
        all_messages = self.log.get_message(0)
        client.send(all_messages.encode())

        while True:
            try:
                message = client.recv(BUFFER_SIZE).decode()
            except:
                print(address, 'disconnected.')
                self.remove_client(client)
                break
            else:
                if message.lower() == 'bye':
                    print(address, 'left chat')
                    formatted_message = f'{ctime()}: [{name}] --> Left Chat'
                    self.log.add_message(formatted_message)
                    with self.lock:
                        self.broadcast(formatted_message, client)
                    self.remove_client(client)
                    break
                else:
                    formatted_message = f'{ctime()}: [{name}] --> {message}'
                    self.log.add_message(formatted_message)
                    with self.lock:
                        self.broadcast(formatted_message, client)

    def start(self):
        print(f"Server is listening on {self.host}:{self.port}")
        while True:
            print('waiting for connection...')
            client_socket, client_address = self.server.accept()
            print(f"New connection from {client_address}")
            with self.lock:
                self.clients.append(client_socket)
            client_thread = Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

host = '127.0.0.1'
port = 5000
server = ChatServer(host, port)
server.start()
