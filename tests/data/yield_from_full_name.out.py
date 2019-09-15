import asyncio

async def coro(future):
    await future
    await asyncio.wait(future)
