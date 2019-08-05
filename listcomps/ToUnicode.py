# 练习列表推导的方式将单个字符转换成 Unicode 代码点

symbols = "欢乐一家人"

codes = [ord(symbol) for symbol in symbols]

print(codes)