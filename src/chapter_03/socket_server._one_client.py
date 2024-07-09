"""
Blocking echo server with sockets one client

References:
https://docs.python.org/3/library/socket.html
"""


import socket

# creates the socket
server_socket = socket.socket(
                              socket.AF_INET,  # address type hostname and port
                              socket.SOCK_STREAM  # communication is with TCP (not UDP)
                              )

server_socket.setsockopt(
    socket.SOL_SOCKET, 
    socket.SO_REUSEADDR, # avoids socket aalready in use error
    1
    )


# socket port binding
server_adress = ("127.0.0.1", 8000)
server_socket.bind(server_adress)

# listent to client connections in the socket
server_socket.listen()


try:

    # waits for a connection and blocks until a connection is stablished
    connection, client_address = server_socket.accept()
    print(f"I got a connection from {client_address}!")


    buffer = b""

    while buffer[-2:] != b"\r\n":
        # receives the data sent through the connection from the client 2 characters at the time
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f"I got data: {data}!")
            buffer = buffer + data
    print(f"All data is : {buffer}")

    # send all the data recived back to the client
    connection.sendall(buffer)
                   
finally:
    server_socket.close()
