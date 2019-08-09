#动态创建类

A = type("A", (object, ), {"a":3})

obj = A()

print(obj.a)

