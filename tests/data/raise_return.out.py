import asyncio


async def coro(x, future):
    if x == 0:
        return 0
    elif x == 1:
        return 1 + 2**3
    elif x == 2:
        return ('a', 'tuple')
    elif x == 3:
        return asyncio.wait(future)
