import asyncio, signal
from asyncio import AbstractEventLoop


from util.delay_functions import delay

def cancel_tasks():
    print("Got a SIGINT")
    # retrieve all the pendings tasks
    tasks: set[asyncio.Task] = asyncio.all_tasks()
    print(f"Cancelling {len(tasks)} task(s).")
    # cancel all pending tasks
    [task.cancel() for task in tasks]


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    # adds a signal handler for SIGINT
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    await delay(10)

asyncio.run(main())
