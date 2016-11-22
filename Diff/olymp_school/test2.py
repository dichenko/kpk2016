with open('list_of_prime.txt') as f:
    data = f.readlines()

data = data[0].split('/n')
print(type(data[3]))
#for i in range(len(data)):
#    data[i] = int(data[i][:-1])

print(len(data))