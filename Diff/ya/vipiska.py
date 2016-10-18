
def sum_el(a,b):
    summa = 0
    global maxi_sum
    arr = mas[a:b]
    for el in arr:
        summa += el
    if summa > maxi_sum:
        maxi_sum = summa


n = int(input())
mas = list(map(int, input().split()))

maxi_sum = mas[0]
for i in range(len(mas)):
    for k in range(len(mas)):
        if i < k:

            sum_el(i,k)

print(maxi_sum)
