def is_2zn(x):
    flag = True
    for i in range(2, len(x)):
        if x[i] != 0:
            if x[i] < 10 or x[i] > 99:
                flag = False
                break
    return flag

def foo(w):
    k = 1
    a = [0]*15
    a[k] = 1
    while w != 85:

        s = 0
        while w != 0:
            c = w % 10
            s += c * c
            w //= 10
        w = s
        k += 1
        a[k] = w

    return k, a
mas_mas = []
mas_i = []
for i in range(20):
    try:
        k,a = foo(i)
        if  k == 5 and is_2zn(a):
            mas_mas.append(a[2:])
            mas_i.append(i)
    except:
        pass

for i in range(len(mas_i)):
    print (mas_i[i], mas_mas[i])

summa = 0
for el in mas_i:
    summa += el;

print(summa)


