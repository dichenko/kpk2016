#http://informatics.mccme.ru/mod/statements/view.php?id=21549#1

n = int(input())
count_of_triangles = 0
star_cords_x = []
star_cords_y = []

for i in range(n):
    a,b = map(int, input().split())
    star_cords_x.append(a)
    star_cords_y.append(b)

for i in range(n):
    x = star_cords_x[i]
    count_of_same_x = star_cords_x.count(x) - 1

    y = star_cords_y[i]
    count_of_same_y = star_cords_y.count(y) - 1

    count_of_triangles += count_of_same_x * count_of_same_y

print(count_of_triangles)





