mas = ["7182818284590452353602874713526624977572470936999595749669676277"]
def sdvig(a):
    return a[1:] + a[0]
for i in range(1,len(mas[0])):
    mas.append(sdvig(mas[i-1]))
mas_sorted = mas.copy()
mas_sorted.sort()
s = ''
for el in mas_sorted:
    s += el[-1]
print(s)



