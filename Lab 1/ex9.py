a = []
for e in range(3):
    a.append(int(input()))
b = list(set(a))
if len(a) == len(b): print(0)
else:print((len(a) - len(b)) + 1)
