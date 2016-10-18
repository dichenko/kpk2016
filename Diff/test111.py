n,x,y = map(int, input().split())
minut = min(x, y)
x, y = min(x, y), max(x, y)
n -= 1
time_1 = n * x
time_2 = 0
i = 1
while time_1 >= time_2:
    time_2 = y * i
    time_1 -=  x
    i += 1
time_1 += x
minut += time_1
print(int(minut))