import trollius
from trollius import Return

@trollius.coroutine
def coro(x, future):
    if x == 0:
        raise Return(0)
    elif x == 1:
        raise Return(1 + 2**3)
    elif x == 2:
        raise Return(('a', 'tuple'))
    elif x == 3:
        raise Return(trollius.wait(future))
