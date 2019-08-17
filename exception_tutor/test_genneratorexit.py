# ??

def g():
    try:
        for i in range(1,10):
            yield i
    except GeneratorExit as e:
        print(e)

gen = g()

for y in gen:
    print(y)
    gen.close()

