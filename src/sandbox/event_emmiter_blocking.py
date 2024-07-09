import asyncio
import random
import logging
from time import sleep
from util import async_timed

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def called_back_function(parent_id, event_param):
    logging.info(f"Entering callback with value  {event_param} called from task {parent_id}")
    sleep(5)
    return



async def emit_event(task_id: str, call_back):

    logging.info(f"Entering emit event in task {task_id}")
    while True:
        logging.info(f"Sleeping task {task_id}")
        await asyncio.sleep(2)
        logging.info(f"Waking up in task {task_id}")
        value =random.normalvariate(0, 10)
        call_back(task_id, value)
        logging.info(f"After executing callback in task {task_id}")


async def main():

    task_1 = asyncio.create_task(emit_event("1", called_back_function))
    task_2 = asyncio.create_task(emit_event("2", called_back_function))
    task_3 = asyncio.create_task(emit_event("3", called_back_function))


    await task_1
    await task_2
    await task_3



asyncio.run(main())

