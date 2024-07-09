import asyncio
import socket

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
    Listen for connections in ani infinite loop. Each time receives one creates a task
    ( echo ) thta reads and echo data from client socket

    """
    while True:
        connection, address = await loop.sock_accept(server_socket)  # blocks untill recevies a connection
        connection.setblocking(False)  # set non-blocking socekt mode
        print(f"Got a connection from {address}")  
        asyncio.create_task(echo(connection, loop))  # scedule an echo task on the event loop for the new socket

async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    while data:= await loop.sock_recv(connection, 1024):  # blocks untill receives data
        print(f"Got data {data.decode('utf-8')}")
        await loop.sock_sendall(connection, data)  # sends back sata to the connected client


asyncio.run(main())