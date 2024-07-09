"""
Preventing tasks to be cancelled regardless a timeout was defined
"""

import asyncio
from my_code.utils import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=1)
        print(result)
    except TimeoutError:
        print("Task took longer than five minutes, it will finish soon!")
        result = await task
        print(result)

asyncio.run(main())


