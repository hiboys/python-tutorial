# 简单协程


def gen(a):
    print(a)
    b = yield a + 2
    print(b)


g = gen(2)
r = next(g)

print("a+2=", r)

g.send(3)
