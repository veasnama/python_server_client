import socket
def create_web_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 80))
    serversocket.listen(5)
    while(1):
        clientsocket, address = serversocket.accept()
        print(address) 

    server.close()

create_web_server()
