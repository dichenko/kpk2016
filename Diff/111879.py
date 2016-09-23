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
    print('counter = ',counter, end = " ")
    for k in range(counter):
        if is_chet(k):
            k = next_chet(data)
            D.append(k)
            print ("k chet =", k)
            data = D[-1]
            if len(D) <= n:
                break
        else:
            k = next_nechet(data)
            D.append(k)
            print("k nechet =", k)
            data = D[-1]
            if len(D) <= n:
                break

print(D[-1])


