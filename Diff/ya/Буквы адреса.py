t = input()

w = ('a', 'e', 'i', 'o', 'u', 'y')

V = ''
C = ""
for buk in t:
    if buk in w:
        V += buk
    else:
        C += buk

if V > C: print('Vowel')
else: print("Consonant")