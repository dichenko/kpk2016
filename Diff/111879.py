#Дана возрастающая последовательность целых чисел 1, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, ...
# Она сформирована следующим образом: берется одно нечетное число, затем два четных,
# затем три нечетных и так далее. Выведите N-й элемент этой последовательности.




def next_chet(x):
    if x % 2 == 0:
        return x + 2
    else: return x + 1


def next_nechet(x):
    return x + 1 + x % 2


def is_chet(x):
    return x % 2 == 0


n = int(input())
D = [1]
data = D[0]
counter = 1
while len(D) <= n:
    counter += 1
    if is_chet(counter):
        for i in range(counter):
            k = next_chet(data)
            D.append(k)
            data = k
            if len(D) <= n:
                D.append('break')
                break
    else:
        for i in range(counter):
            k = next_nechet(data)
            D.append(k)
            data = k
            if len(D) <= n:
                D.append('break')
                break

print(D)


