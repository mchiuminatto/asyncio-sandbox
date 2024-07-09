import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

# register the SERVER socket with the selector, for read events
selector.register(server_socket, selectors.EVENT_READ)  

while True:
    #A creates a selector  timing out after 1 second
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1) 

    #B if no events to process prints a message. This happens after time out
    if len(events) == 0: 
        print("No events, waiting a bit more!")

    for event, _ in events:
        #C  get the socket number from this structure
        event_socket = event.fileobj 

        #D   if the socket number is the SERVER socket, then is a connection attempt thta need to be accepted
        if event_socket == server_socket: 
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"I got a connection from {address}")
            #E  register the CLIENT socket with the selector
            selector.register(connection, selectors.EVENT_READ) 
        else:
            #F  the socket was the client's so we receive the data
            data = event_socket.recv(1024) 
            print(f"I got some data: {data}")
            event_socket.send(data)
