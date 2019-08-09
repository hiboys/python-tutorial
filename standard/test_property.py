# 定义类的托管属性，也就是可以通过 get set 来进行拦截
# 类似 java 中的 getter 和 setter

class C(object):
    def getx(self): return self._x

    def setx(self, value): self._x = value

    def delx(self): del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

c = C()

c.x = 3

print(c.x)