#dict 的 setdefault 正确用法
#如果一个 key 不存在，把default value 放到 dict 中，并且返回这个 value
#可以用于链式方格写

d = dict()

d.setdefault("name", []).append("wuyixiong")

print(d)