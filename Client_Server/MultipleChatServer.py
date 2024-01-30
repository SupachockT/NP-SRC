from socket import*
from threading import Thread
import threading
from time import ctime

class chatRecord():
    def __init__(self):
        self.data = []
        
    def addMessage(self, message):
        self.data.append(message)
        
    def getMessage(self, messageID):
        if len(self.data) == 0:
            return "No message yet!"
        elif messageID == 0:
            return '\n'.join(self.data)
        elif messageID != 0:
            temp = self.data[messageID]
            return '\n'.join(temp)
        else:
            return '\n'

class clientHandler(Thread):
    def __init__(self, client, record, address):
        Thread.__init__(self)
        self._client = client
        self._record = record
        self.address = address
    
    def broadCastingMessage(self, activeClient, message):
        for socket in CONNECTION_LIST:
            if socket != server and socket != activeClient:
                try:
                    broadcastMessage = str.encode(message)
                    socket.send(broadcastMessage)
                except:
                    print("Client %s is offine" % self.address)
                    broadcastMessage(socket, ("Client %s is offine" % self.address))
                    socket.close()
                    CONNECTION_LIST.remove(socket)
                    
    def run(self):
        self._client.send(str.encode('Welcome to the chat room'))
        self._name = bytes.decode(self._client.recv(BUFSIZE))
        allMessage = self._record.getMessage(0)
        self._client.send(str.encode(allMessage))
        while True:
            message = bytes.decode(self._client.recv(BUFSIZE))
            if not message or message.lower() == "bye":
                print(self.address, "left chat")
                self._client.close()
                CONNECTION_LIST.remove(self._client)
                break
            else:
                message = ctime() + ': [' + self._name + '] -->' + message
                self._record.addMessage(message)
                threadLock.acquire()
                self.broadCastingMessage(self._client, message)
                threadLock.release()

hostname = gethostname()
ip_address = gethostbyname(gethostname())
port = 5000
BUFSIZE = 4096
ADDRESS = (hostname, port)
CONNECTION_LIST = []
threadLock = threading.Lock()

record = chatRecord()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(10)
CONNECTION_LIST.append(server)
print("Chat server started on: ", hostname, ip_address, str(port))

while True:
    print("Waiting for connection...")
    client, address = server.accept()
    print("...connected from: ", address)
    #Lock CONNECTION_LIST for inserting connected client
    threadLock.acquire()
    CONNECTION_LIST.append(client)
    #Release CONNECTION_LIST
    threadLock.release()
    handler = clientHandler(client, record, address)
    handler.start()
    

