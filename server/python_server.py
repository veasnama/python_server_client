import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 9000))

server_socket.listen(5)

while True:
    (client_socket, address) = server_socket.accept()
    print(f"New connection from client {client_socket}")

    chunks = []
    while True:
        data  = client_socket.recv(2048)
        if not data:
            break;
        chunks.append(data)
    client_socket.sendall(b''.join(chunks))
    client_socket.close()

