import asyncio

async def main():
    await asyncio.sleep(1)

event_loop = asyncio.new_event_loop()

try:
    event_loop.run_until_complete(main())

finally:
    event_loop.close()