#有五种方式可以构建一个 dict

#通过命名参数来构建字典
a = dict(first_name="yixiong", last_name="wu")

print(a)

#通过二元祖来构建字典
a = dict([("first_name", "yixiong"), ("last_name", "wu")])

print(a)

#通过列表来构建字典
keys = ["first_name", "last_name"]
values = ["yixiong", "wu"]

a = dict(zip(keys, values))

print(a)

#通过字面量来构造字典
a = dict({"first_name":"yixiong", "last_name":"wu"})

print(a)

#通过字典推导来构建
a = { k: v for k, v in zip(keys, values)}

print(a)

