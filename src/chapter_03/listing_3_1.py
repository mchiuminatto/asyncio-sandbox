import socket

# creates the socket in the server
# with address system ip:port AF_NET
# we use TCP protocol (not UDP) SOCK_STREAM
# we reuse the port number after restartig the application:SO_REUSEADDR

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# this sets and bind the addressing system to the socket
# finally listent to clinet connection
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

# when a request is received to the server socket, creates a new socket 
# for communication with the clinet
connection, client_address = server_socket.accept()
print(f'I got a connection from {client_address}!')
server_socket.close()
