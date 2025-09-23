import time

import pytest

from src.async_writer.synch_writer import Writer as SynchWriter
from src.async_writer.asynch_writer import Writer as AsynchWriter
import logging
import asyncio

RECORDS_SYNC = 15000000
RECORDS_ASYNC = 100000000

def test_writer_synch():

    time_0 = time.time()
    wr = SynchWriter(RECORDS_SYNC)
    wr.coordinate()
    duration = time.time() - time_0
    logging.info(f"Execution lasted {duration}")

    assert True

@pytest.mark.asyncio
async def test_writer_asynch():

    time_0 = time.time()
    wr = AsynchWriter(RECORDS_ASYNC)
    await wr.coordinate()
    duration = time.time() - time_0
    logging.info(f"Execution lasted {duration}")

    assert True