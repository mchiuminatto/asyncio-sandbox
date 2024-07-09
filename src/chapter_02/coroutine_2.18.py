import asyncio
from util import async_timed
from util import delay



@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


@async_timed()
async def main():
    task_1 = asyncio.create_task(cpu_bound_work())
    task_2 = asyncio.create_task(cpu_bound_work())
    await task_1
    await task_2

asyncio.run(main())
