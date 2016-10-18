"""http://informatics.mccme.ru/mod/statements/view3.php?id=21367&chapterid=112811#1"""


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


def find_piece(mas):
    """
    Находит в списке первую ненулевую последовательность
    возвращает срез
    индекс начала среза
    индекс конца среза
    :param mas:
    :return: srez, i_start, i_finish
    """

    i_start = 0
    i_finish = len(mas) - 1

    srez = []
    was_find = False
    if mas[0] == 0:
        posled = False
        lenght = 0
    else:
        posled = True
        lenght = 1

    for i in range(1, len(mas) - 1):
        if mas[i] != 0 and mas[i + 1] != 0 and posled is False:
            posled = True
            i_start = i
            lenght += 1
        elif mas[i] != 0 and mas[i + 1] != 0 and posled is True:
            i_finish = i + 1
            lenght += 1
        elif mas[i] != 0 and mas[i + 1] == 0 and posled is True:
            i_finish = i
            lenght  +=1
            posled = False
            was_find = True
        if lenght > 0 and was_find:
            break
    else:
        posled = True
        lenght = 1
    return mas[i_start:i_finish+1], i_start, i_finish+1


    #print('i_start =', i_start, "i_fin =", i_finish)
    #print(mas[i_start], ':', mas[i_finish])

global_counter = 0
n = int(input())
mas = []
for i in range(n):
    mas.append(int(input()))

while in_process(mas):
    q, start, finish = find_piece(mas)
    q = vichet(q)
    mas[start:finish] = q

print(global_counter)


mas = [0,3,5,7,0,5,3, 9]
print(find_piece(mas))


