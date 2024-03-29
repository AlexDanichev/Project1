class Test:

    def __init__(self, x):
        self._x = x
   #     self._y = y
    #    self._z = z

    @property
    def x(self):
        print("GETTER CALLED")
        return self._x

    @x.setter
    def x(self, x):
        print("SETTER CALLED")
        if x > 10:
            raise ValueError("X must be less then 10")
        self._x = x

    @x.deleter
    def x(self):
        print("DELETER CALLED")
        del self._x


obj = Test(100)

obj.x
obj.x = 8
del obj.x