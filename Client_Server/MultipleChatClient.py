from socket import*

BUFSIZE = 4096
server = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 5000
ADDRESS = (host, port)

server.connect(ADDRESS)
messageFromServer = bytes.decode(server.recv(BUFSIZE))
print(messageFromServer)

name = input("Enter your name: ")
userName = str.encode(name)
server.send(userName)

while True:
    msgR = bytes.decode((server.recv(BUFSIZE)))
    if not msgR:
        print("Server disconnected")
        break
    print(msgR)
    
    send_message = input('> ')
    if not send_message:
        print('Server disconnected')
        break
    server.send(str.encode(send_message))
server.close()