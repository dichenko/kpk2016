def is_2zn(x):
    flag = True
    for i in range(2, len(x)):
        if x[i] < 10 or x[i] > 99:
            flag = False
            break
    print(flag)
    return flag

a = [1,1,34,45,56]
s = [0,0,123,4,56]
is_2zn(a)
is_2zn(s)