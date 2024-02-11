from threading import Thread
from socket import *

host = '127.0.0.1'
port = 5000

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            # Handle the exception gracefully
            pass

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}.')

        client.send('nickname'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = Thread(target=handle, args=(client,))
        thread.name = f'client {nickname}'
        thread.start()

print('Server is listening...')
receive()
