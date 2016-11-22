import math
def is_prime(x):
    est_deliteli = False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            est_deliteli = True
            break
    return not(est_deliteli)

list_of_prime = []
for i in range(2, 10000000):
    if is_prime(i):
        list_of_prime.append(i)

with open('list_of_prime.txt', 'w') as f:
    for el in list_of_prime:
        f.write(str(el)+'/n')



