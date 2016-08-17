class Vector2D():
    def __init__(self,x=0,y=0):
        self._x = x
        self._y = y
    def plus(self,other):
        x = self._x + other.x
        y = self._y + other.y
        return Vector2D(x,y)
