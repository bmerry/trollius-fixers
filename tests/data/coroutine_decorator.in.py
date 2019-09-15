import trollius

@trollius.coroutine
def coro():
    pass

@trollius.coroutine
def coro_with_args(a, b, *args, **kwargs):
    pass

class A:
    @trollius.coroutine
    def coro_method(a):
        pass
