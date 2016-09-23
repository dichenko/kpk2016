#http://informatics.mccme.ru/moodle/mod/statements/view3.php?chapterid=623&run_id=32r91814#1
from math import sqrt


def min_del(x):
    '''
    Возвращает минимальный делитель
    :param x: int
    :return: int minimal divider
    '''
    flag = False
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            flag = True
            break
    if flag: return i
    else: return x


x = int(input())
D = []
i = 0
k = x
flag = False
while x > 1 :
    d = min_del(x)
    D.append(d)
    x = x // d


for i in range(len(D)-1):
    print(D[i],"*", sep = "", end = "")
print(D[-1])


