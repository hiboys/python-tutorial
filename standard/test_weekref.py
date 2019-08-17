import weakref

old = {1, 2, 3}
a = weakref.ref(old)
print(a())
del old

print(a())

cache_dict = {}


def cached(key, func):
    if key in cache_dict:
        ref = cache_dict[key]()
        if ref is not None:
            print("old")
            return ref
    print("new")
    r = func()
    cache_dict[key] = weakref.ref(r)
    return r


class A:
    pass


def get_count():
    return A()


a = cached("get_count", get_count)

print(a)


b = cached("get_count", get_count)

print(b)

a = A()

a_ref = weakref.ref(a)

print(a_ref())

del a

a = None

print(a_ref())


