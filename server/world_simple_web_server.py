from socket import *


def create_server():

    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while True:
            print("start listenning.....")
            (client_socket, address) = server_socket.accept()
            rd = client_socket.recv(5000).decode()
            data = rd.split("\n")
            if len(data) > 0: print(data[0])
            
            res_data = "HTTP/1.1 200 OK\r\n"
            res_data += "Content-Type: text/html; charset=utf-8\r\n"
            res_data += "\r\n"
            res_data += "<html> <body> <h1>Hello from server</h1> </body></html>\r\n\r\n"
            client_socket.sendall(res_data.encode())
            client_socket.shutdown(SHUT_WR)
            
    except KeyboardInterrupt:
        print("Close server by interrupt key")
    except Exception as exc:
        print("Error: \n")
        print(exc) 
    server_socket.close() 
print("Access http://localhost:9000")
create_server()
