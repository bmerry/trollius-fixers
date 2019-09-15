import trollius

class A:
    @classmethod
    @trollius.coroutine
    def coro():
        pass
