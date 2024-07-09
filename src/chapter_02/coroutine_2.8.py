"""
Create a task that can run concurrently
"""

import asyncio
from my_code.utils import delay


async def main():
    # here we run the task
    sleep_for_three = asyncio.create_task(delay(3))  # returns a task object
    print("type ", type(sleep_for_three))
    # here we pause to wait for the task to return
    result = await sleep_for_three
    print(result)


asyncio.run(main()) 1