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


mas = [1,3,5,7,0,5,3, 9]
print(find_piece(mas))