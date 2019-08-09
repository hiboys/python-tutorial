# zip 生成的列表长度是最短的长度

s1 = [1,2,3,4]
s2 = [2,3,4]
for t in zip(s1, s2):
    print(t[0], t[1])