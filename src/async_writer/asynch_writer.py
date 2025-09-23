import random
import string
import asyncio
import logging


class Writer:

    def __init__(self, records = 1000):
        self._data = list()
        self._records = records

    async def write(self):
        logging.info("Asynchronous writing started")
        file_id = "".join([random.choice(string.digits) for _ in range(10)])
        with open(f"async_{file_id}_output.txt", "a") as f:
            for record in self._data:
                f.write(record + "\n")
            f.flush()

    async def produce(self):
        logging.info("Asynchronous production started")
        for i in range(self._records):
            record = f"record-{i} {random.randint(0, self._records)}"
            self._data.append(record)

    async def coordinate(self):
        task_1 = asyncio.create_task(self.produce())
        task_2 = asyncio.create_task(self.write())

