A = []
for i in range(1,100):
    x = str(11**i)
    A.append(x)

def contain_11(x, y):
    """проверяет, содержит ли число х число y """
    return str(y) in str(x)

def is_bez_11(x):
    """функция проверяет, является ли число без-11"""
    bez_11 = True
    for i in range(len(str(x))+2):
        if contain_11(x, A[i]):
            bez_11 = False
            break
    return bez_11


if __name__ == "__main__":
    counter = 0
    g = 500
    for i in range(1,g+1):
        if not is_bez_11(i):
            counter += 1
    print(counter+1+g)






