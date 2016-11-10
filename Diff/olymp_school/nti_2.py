

def foo(w):
    k = 1
    a = [0]*100000000
    a[k] = 1
    while w != 85:
        print('big cycle start')
        s = 0
        while w != 0:
            c = w % 10
            s = s + c * c
            w = w // 10
            print ('small cycle', c,s,w)
        w = s
        k += 1
        a[k] = w
        print('big cycle finish')
    return k


print(foo(17))

