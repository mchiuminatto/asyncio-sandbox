"""
Example of using wait_for to handle timeout, which is more simple
than manually

"""

import asyncio
from my_code.utils import delay


async def main():
    delay_task = asyncio.create_task(delay(2))  # we create an awaitable
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)  # wait for the task
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Got a timeout")
        print(f"Was the task cancelleld? {delay_task.cancelled()}")  # the task keeps track of a cancelled status


asyncio.run(main())
