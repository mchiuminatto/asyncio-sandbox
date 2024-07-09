"""
Execute two coroutines concurrently and while they
run we print some messages

"""

import asyncio
from my_code.utils import delay


async def hello_every_second():
    for i in range(5):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting")


async def main():
    # run two concurrent tasks
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    # print messages while other tasks are running
    await hello_every_second()
    # wait for the results of the running tasks
    await first_delay
    await second_delay


asyncio.run(main())
