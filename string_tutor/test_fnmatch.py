from fnmatch import fnmatch

##处于简单的字符串匹配和全功能的正则表达式匹配之间的一种解决方案

result = fnmatch('foo.txt', '*.txt')
print(result)

result = fnmatch('foo.txt', '?oo.txt')
print(result)

result = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(result)