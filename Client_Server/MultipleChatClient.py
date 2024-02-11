import socket
from threading import Thread

BUFFER_SIZE = 4096

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode()
            if not message:
                print("Disconnected from server.")
                break
            print(message)
        except:
            print('Server disconnected')
            break

def send_messages(client_socket):
    while True:
        try:
            sendMessage = input('\n> ')
            if not sendMessage:
                print('Server disconnected')
            elif sendMessage.lower() == '> bye':
                break
            client_socket.send(sendMessage.encode())
        except:
            print('client side error')

def main(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print("Connected to server.")
    except:
        print('Error connecting to server')
        return
    
    serverMessage = bytes.decode(client_socket.recv(BUFFER_SIZE))
    print(serverMessage)
    userName = input('Enter your name: ').encode()
    client_socket.send(userName)

    try:
        receive_thread = Thread(target=receive_messages, args=(client_socket,))
        send_thread = Thread(target=send_messages, args=(client_socket,))

        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()
    finally:
        client_socket.close()

if __name__ == "__main__":
    main(host='127.0.0.1', port=5000)