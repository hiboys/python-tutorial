#返回局部命名空间符号表
print(vars())

class A:
    a = 3

    def __init__(self):
        self.b = 1

    def my_print(self):
        pass

a = A()

# 返回 A 的成员变量 self.b
print(vars(a))
