c = int(input())
chet = (c % 2 == 0) * ((c // 2 * 5) + ((c//2 - 1)* 15))
nechet = (c % 2 != 0) * (c // 2 * 5 + c // 2 * 15)
b = ((45 * c) % 60 + chet % 60 + nechet % 60)
a = 9 + (45 * c) // 60 + chet // 60 + nechet // 60 + b // 60
b = b % 60
print(a, b)
