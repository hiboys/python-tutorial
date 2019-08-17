from collections import defaultdict

class MyDict(defaultdict):

    def __missing__(self, key):
        pass

dd = MyDict(int);

# 在 dict 的方法中，只有__getitem__会触发__missing__方法的调用
# get 方法默认不会触发__missing__方法调用，触发重写
dd["wuyixiong"] = dd["wuyixiong"] + 1

a = dd.get("wuyixiong")

print(a)