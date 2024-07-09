#!/usr/bin/env python3
import asyncio
import random
import logging
from time import sleep
from util import async_timed

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


async def main():

    task_collector = {}
    for i in range(1,4):
        task_collector[i] = asyncio.create_task(task_execution(str(i)))
        

    for task_id in task_collector:
        await task_collector[task_id]


async def task_execution(task_id: str):
    logging.info(f"Executing task {task_id}")

    task = asyncio.create_task(event_emmiter(str(task_id)))
    task.add_done_callback(called_back_function)
    
    logging.info(f"Awaiting task {task_id} execution")
    await task
    logging.info(f"Executed task {task_id}")


async def event_emmiter(task_id):

    logging.info(f"Emmiting event for task {task_id}")
    logging.info(f"Sleeping task {task_id}")
    await asyncio.sleep(2)
    logging.info(f"Waking up task {task_id}")
    value = random.normalvariate(0, 10)
    result = {}
    result["task"] = task_id
    result["value"] = value
    
    return result

def called_back_function(future):
    result = future.result()
    task_id = result["task"]
    value = result["value"]

    logging.info(f"Entering callback with value {value} called from task {task_id}")
    sleep(5)
    
    logging.info(f"Processing result from task {task_id}, {value}")
    return


asyncio.run(main())


# TODO: Loop emmiting events

