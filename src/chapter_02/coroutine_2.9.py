"""
This runs multiple tasks concurrently
"""

import asyncio
from my_code.utils import delay


async def main():

    # we start three tasks concurrently
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    # now we wait for the results of the three concurrently running tasks
    await sleep_for_three
    await sleep_again
    await sleep_once_more


asyncio.run(main())
