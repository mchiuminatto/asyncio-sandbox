
import asyncio

from util.async_timer import async_timed

@async_timed()
async def cpu_bound_work() -> int:

    counter = 0

    for i in range (100000000):
        counter += 1
    return counter

async def main() -> None:

    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.001
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one

asyncio.run(main(), debug=True)



