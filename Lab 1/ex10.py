a = []
for e in range(3):
    a.append(int(input()))
a = list(map(str,sorted(a)))
print(' '.join(a))
