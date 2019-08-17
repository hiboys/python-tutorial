
# 为不存在的属性赋值，会出现属性错误
# 此异常关乎数据状态

try:
    a=object()
    a.b = 3
except AttributeError as e:
    print(e)