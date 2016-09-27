#http://informatics.mccme.ru/mod/statements/view.php?id=21549#1

n = int(input())

#Создаем список кортежей, где будут храниться координаты точек
star_cords = []

# создаем список треугольников
triangle_list = []

def find_all_triangles(star_cords, N):
    """
    Получает на вход список с координатами и номер текущей звезды,
    Записывает в глобальный список треугольников все возможные треугольники для этой точки
    (в отсортированном виде)
    :param star_cords: список кородинат звезд
    :param N: номер текущей звезды
    :return: 0
    """
    global triangle_list
    same_x = []
    same_y = []
    for i in range(len(star_cords)):  #Перебираем все координаты к
        if i != N:                    #роме текущей
            if star_cords[i][0] == star_cords[N][0]:
                same_x.append(i)   #Добавляем в список звезды с таким же X
            elif star_cords[i][1] == star_cords[N][1]:
                same_y.append(i)   #Добавляем в список звезды с таким же Y
    #Генерируем список треугольников по полученным спискам точек
    for x in same_x:
        for y in same_y:
            tr = [x,y,N]
            tr.sort()
            triangle_list.append(tr)




#принимаем координаты и упаковываем в список
for i in range(n):
    a,b = map(int, input().split())
    star_cords.append([a,b])

for i in range(len(star_cords)):
    find_all_triangles(star_cords, i)

print(len(triangle_list))




