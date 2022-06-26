from socket import *

def create_simple_browser():

    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 9000))
        cmd = 'GET http://localhost HTTP/1.0\r\n\r\n'.encode()
        client_socket.send(cmd)
        while 1:
            data = client_socket.recv(512);
            if len(data) < 1:
                break;
            print(data.decode(), end=" ")
    except KeyboardInterrupt:
        print("Shutdown the program")
    except Exception as exc:
        print("Error: \n")
        print(exc)
    client_socket.close()
create_simple_browser()


