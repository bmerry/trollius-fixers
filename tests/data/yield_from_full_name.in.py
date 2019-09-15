import trollius

@trollius.coroutine
def coro(future):
    yield trollius.From(future)
    yield trollius.From(trollius.wait(future))
