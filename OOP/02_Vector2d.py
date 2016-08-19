class Vector2D():
    def __init__(self,x=0,y=0):
        self._x = x
        self._y = y
    def __add__(self,other):
        '''
        #Переопределяем стандартный метод, чтобы сложение векторов
        давало нам именно то что мы хотим
        :return: метод отвечает за операнд "+", складывая координаты.
        '''
        x = self._x + other._x
        y = self._y + other._y
        return Vector2D(x,y)

    def __str__(self):
        """Переопределяем Print для класса
        :return: #отвечает за то что ббудет выведено на печать при печати экземпляра класса
        """
        return '(%d, %d)'%(self._x, self._y)

    def __mul__(self,other):
        """Переопределяем умножение для класса"""
        x = self._x * other._x
        y = self._y * other._y
        return Vector2D(x+y)

a = Vector2D(2,2)
b = Vector2D(-1,3)
c = a * b

print(a, '*', b, '=',c)
