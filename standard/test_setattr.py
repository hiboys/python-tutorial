a= object()

# 如果属性不存在，会报错
# setattr(a, "b", 3)

# print(a.b)

class A:

    def __init__(self):
        self.b = None

a = A()

setattr(a, "b", 3)

print(a.b)