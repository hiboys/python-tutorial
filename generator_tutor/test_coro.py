class DemoExcept(Exception):
    '''异常类型'''


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoExcept:
            print('*** DemoExecpt handled Contiuing....')
        else:
            print('-> coroutine received: {!r}'.format(x))
    # 一旦出现未处理异常，协程会立刻终止，这行代码应该永远不会执行
    raise  RuntimeError('this line should never run.')

excc_coro = demo_exc_handling()
next(excc_coro)
excc_coro.send(11)
excc_coro.send(22)
excc_coro.throw(ZeroDivisionError)
from inspect import getgeneratorstate

print(getgeneratorstate(excc_coro))