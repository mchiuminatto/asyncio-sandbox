import random
import string
import logging


class Writer:

    def __init__(self, records = 1000):
        self._data = list()
        self._records = records

    def write(self):
        logging.info("Synchronous writing started")
        file_id = "".join([random.choice(string.digits) for _ in range(10)])
        with open(f"sync_{file_id}_output.txt", "a") as f:
            for record in self._data:
                f.write(record + "\n")
            f.flush()

    def produce(self):
        logging.info("Synchronous production started")
        for i in range(self._records):
            record = f"record-{i} {random.randint(0, self._records)}"
            self._data.append(record)


    def coordinate(self):
        self.produce()
        self.write()
