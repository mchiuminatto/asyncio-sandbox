import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return "hello world"


async def main() -> None:
    message = await hello_world_message()
    print("waiting for ... ")
    print(message)


asyncio.run(main())

