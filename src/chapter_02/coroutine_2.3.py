import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


# coroobj = coroutine_add_one(10)
# print(coroobj)
result = asyncio.run(coroutine_add_one(2))
print(result)

