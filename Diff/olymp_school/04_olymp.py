mas = [int(input()) for i in range(int(input()))]

mas_1 = [0]

i_vverh = None
i_vniz = None


for i in range(1, len(mas)):
    if mas[i] > mas[i-1]:
        mas_1.append(1)
    elif mas[i] == mas[i-1]:
        mas_1.append(0)
    else:
        mas_1.append(-1)


for i in range(1, len(mas)-1):
    if mas_1[1] == 1 and mas_1[i+1] != 1 :
        i_vverh = i
        break
if i_vverh:
    for i in range(i_vverh, len(mas)-1):
        if mas_1[i] == -1:
            i_vniz = i
            break

if i_vniz and i_vverh:
    print(i_vverh)
    print(i_vniz + 1)
else:
    print(0)