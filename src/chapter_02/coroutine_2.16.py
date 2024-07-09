import functools
import time
import asyncio



def async_timed():
    def wrapper(func: callable) -> callable:

        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            print(f"starting {func} with args {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"finished {func} in {total: .4f} seconds(s)")

        return wrapped
        
    return wrapper


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two


@async_timed()
async def delay(delay_seconds: int):
    print(f"sleeping for {delay_seconds} second(s)")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} second(s)")
    return delay_seconds



asyncio.run(main())