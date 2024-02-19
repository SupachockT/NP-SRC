from socket import*

def ClientConnectServer(host, port):
    address = (host, port)
    
    server = socket(AF_INET, SOCK_STREAM)
    server.connect(address)
    return server

host = gethostname()
port = 8000
bufferSize = 1024

server = ClientConnectServer(host, port)
#Recieve from server
serverMessage = bytes.decode(server.recv(bufferSize))
print(serverMessage)

#Chat with server
while True:
    m = input(' > ')
    server.send(str.encode(m))
    if not m:
        break
    
    reply = bytes.decode(server.recv(bufferSize))
    if not reply:
        print("Server disconnected")
        break
    print("Server said:", reply)

server.close()
print("Left chat")
