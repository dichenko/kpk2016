#http://informatics.mccme.ru/mod/statements/view3.php?id=586&chapterid=723#1

a = input()
a = a[:-1]
a_list = []
b_list = [0]*len(a_list)
for letter in a:
    a_list.append(letter)

start = 0
end = len(a_list)-1
for i in range(len(a_list)):
    if i % 2 == 0:
        b_list[start] = a_list[start]
        start += 1
    else:
        b_list[end] = a_list[end]
        end -= 1

print(a_list)
print(b_list)




