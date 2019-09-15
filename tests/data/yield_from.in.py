import trollius
from trollius import From

@trollius.coroutine
def coro(future, foo):
    yield From(future)
    yield From(foo.future)
    yield From(func())
    yield From(a + b)
    yield From(a**b)
    yield From(a if x else y)
