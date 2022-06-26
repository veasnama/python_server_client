import socket

# create a socket connection liek a phone

socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_conn.connect(("www.google.com", 80))
cmd = 'GET http://www.google.com/ HTTP/1.0\r\n\r\n'.encode()
socket_conn.send(cmd)

while True:
    data = socket_conn.recv(512)
    if len(data) < 1:
        break;
    print(data.decode(), end='')
socket_conn.close()

