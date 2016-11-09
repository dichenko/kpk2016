#max weight of backpack
s = int(input())
n = int(input())
backpack = 0
case = 0
for i in range(n):
    x = int(input())
    limit = s - backpack
    if x < limit:
        backpack += x
    else:
        case += x


print(backpack)
print(case)



