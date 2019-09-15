import asyncio


async def coro(future, foo):
    await future
    await foo.future
    await func()
    await (a + b)
    await (a**b)
    await (a if x else y)
