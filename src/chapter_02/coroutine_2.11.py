"""
Example of task cancellation handled manually
"""

import asyncio
from asyncio import CancelledError
from my_code.utils import delay


async def main():

    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():  # dome method is True if the task is done, False Otherwise
        print("Task not finished, checking again in a second")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            print("cancelling task")
            long_task.cancel()  # manually cancelling the task

    try:
        await long_task  # only here the task cancellation will be spotted amd the error raised
    except CancelledError:
        print("Our task was cancelled")


asyncio.run(main())

