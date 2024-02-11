from threading import Thread
from socket import *

host = '127.0.0.1'
port = 5000

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

nickname = input('Choose a nickname: ')

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'nickname':
                client.send(nickname.encode('ascii'))  # Encode the nickname before sending
            else:
                print(message)
        except Exception as e:
            print(f'An error occurred: {e}')
            client.close()
            break

def write():
    while True:
        message = input('')
        if message.lower() == 'exit':  # Graceful exit if user types 'exit'
            client.close()
            break
        full_message = f'{nickname}: {message}'
        client.send(full_message.encode('ascii'))

receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()
