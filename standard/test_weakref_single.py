# 从 pycharm 调试，第二次还是输出同个对象，怀疑是调试器持有对象的引用

import weakref


class A:

    def __init__(self):
        self.b = "hello"


a = A()

ar = weakref.ref(a)

print(ar)


print(ar())


del a


print(ar())
