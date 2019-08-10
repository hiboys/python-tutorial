# 函数式编程
# attrgetter 适用于一组序列，对外表现出一致的属性

from operator import attrgetter
from collections import namedtuple

Name = namedtuple("Name", ["first_name", "last_name"])

my_name = Name(first_name="yixiong", last_name="wu")

first_name = attrgetter("first_name")

print(first_name(my_name))