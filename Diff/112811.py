"""http://informatics.mccme.ru/mod/statements/view3.php?id=21367&chapterid=112811#1"""
global_counter = 0

def vichet(mas):
    """
    Принимаем массив, находим минимальный элемент, вычитаем минимальный эл из каждого эл.
    Увеличиваем global_counter на величину x * (len(mas) - 1)
    :param mas:
    :return: измененный mas
    """
    global global_counter
    min_el = min(mas)
    for i in range(len(mas)):
        mas[i] -= min_el
    global_counter += min_el * (len(mas) -1 )
    return mas


def in_process(mas):
    """
    Проверяет, есть ли смысл дальше работать с этим массивом.
    Если в маассиве есть хотя бы два подряд ненулевых элемента, то работаем
    :param mas: массив с ненулевыми элементами
    :return: возвращает True если с массивом можно дальше работать
    """
    flag = False
    for i in range(1,len(mas)):
        if mas[i] != 0 and mas[i-1] != 0:
            flag = True
            break
    return flag



n = int(input())
mas = []
for i in range(n):
    mas.append(int(input()))
print(mas)


x = min(mas)
print(x)
counter = (n-1) * x

for i in range(n):
    mas[i] = mas[i] - x

print(mas)
print('counter =', x)




