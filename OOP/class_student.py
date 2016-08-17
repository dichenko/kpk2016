#Инкапсуляция: данные и код зашиваются внутрь объекта, это дает возможностьсокрытия данных
class Student():
    def __init__(self, name, age):
        self.__name = name#приватный атрибут
        self.__age = age #приватный атрибут
    def aging(self):  #Метод меняет приватный артибут
        self.__age += 1
        print(self.__age)

p = Student('Peter', 18)
s = Student('Sly', 17)
s.aging()

