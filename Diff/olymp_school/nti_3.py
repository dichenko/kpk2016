a = list(input().split())
rate = float(a[0])
power = int(a[1])
a_std1 = "7E7E7E7E7E7E7E7E"
a_std2 = "1E1E"
rate = str(hex(int((rate-422.4)*10)))[2:].upper()
if len(rate)< 2: rate = "0" + rate
if power == -10: power = "00"
elif power == -2: power = "01"
elif power == 6: power = "02"
elif power == 10: power = "03"
print(a_std1+rate+power+a_std2)

