import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'I got a connection from {client_address}!')

    buffer = b''

    # read from socket buffer until fonds a carrieage return + line feed in the last 2 characters
    while buffer[-2:] != b'\r\n':
        # here receives the data from the buffer
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f'I got data: {data}!')
            # appends the rading buffer to the full buffer.
            buffer = buffer + data

    print(f"All the data is: {buffer}")
finally:
    server_socket.close()
