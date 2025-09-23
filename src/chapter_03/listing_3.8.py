import asyncio
import socket
import logging

from asyncio import AbstractEventLoop


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # set up the server socket
    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    # fires the listening task
    await listen_for_connection(server_socket, asyncio.get_event_loop())

async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    """
    Listen for connections in an infinite loop. Each time receives one creates a task
    ( echo ) that reads and echo data from/to client socket

    """
    while True:
        # blocks untill recevies a connection
        connection, address = await loop.sock_accept(server_socket)  
        # set non-blocking socekt mode
        connection.setblocking(False)  
        print(f"Got a connection from {address}")  
        # scedule an echo task on the event loop for the new socket
        asyncio.create_task(echo(connection, loop))

async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        # blocks untill receives data
        while data:= await loop.sock_recv(connection, 1024):  
            print(f"Got data {data.decode('utf-8')}")
            if data.decode('utf-8') == "boom\r\n":
                raise Exception("Unexpected network error")
            # sends back data to the connected client
            await loop.sock_sendall(connection, data)  
    except Exception as ex_instance:
        logging.exception(ex_instance)
    finally:
        connection.close()


asyncio.run(main())
