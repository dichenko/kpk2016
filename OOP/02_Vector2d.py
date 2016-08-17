class Vector2D():
    def __init__(self,x=0,y=0):
        self._x = x
        self._y = y
    def plus(self,other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector2D(x,y)
    def __str__(self):
        """
        :return: #отвечает за то что ббудет выведено на печать при печати экземпляра класса
        """
        return '('+str(self._x)+'; '+str(self._y)+')'

a = Vector2D(2,2)
b = Vector2D(-1,3)
c = a.plus(b)

print(a, '+', b, '=',c)
