n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

u = [0,0,0]

u[0] = m[0][1]
u[1] = m[0][2]
u[2] = m[0][3]

print(*u)

for i in range(1,n):
    pass
    #FIXME!!!!
