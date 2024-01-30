from socket import*

def ServerInit(host, port):
    address = (host, port)
    
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(address)
    server.listen(2)
    return server
            
host = gethostbyname(gethostname()) #IPv4
port = 8000
bufferSize = 1024

server = ServerInit(host, port)

#Part 1
message = "Welcome to Chat Application. \nWho are you?"
print("server address: " + host + "\nServer Port: " + str(port))
print("Waiting for connection...")
client, address = server.accept()
print("Connected from:", address)
client.send(str.encode(message)) #server send data to client

#Part 2
while True:
    m = bytes.decode(client.recv(bufferSize))
    if not m:
        print("Client disconnected")
        client.close()
        break
    else:
        print("Client said:", m)
        client.send(str.encode(input(' > ')))

