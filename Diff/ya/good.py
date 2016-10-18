def sounds_good(s):
    """
    Увеличивает global counter на 1 если
    слово строка сожержит две подряд гласные буквы
    """
    global counter
    let = ('a', 'e', 'i', 'o', 'u')
    for i in range(len(s) - 1):
        if s[i] in let and s[i + 1] in let:
            counter += 1
            break


n = int(input())
mas = list(input().split())
counter = 0

for i in range(len(mas)):
    mas[i] = mas[i].lower()

new_mas = []
for el in mas:
    if el not in new_mas:
        new_mas.append(el)

for el in new_mas:
    sounds_good(el)

if counter >= n:
    print(0)
else:
    print(n - counter)

