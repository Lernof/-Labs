a = int(input())
b = int(input())

arr = [str(e) for e in range(a, b+1) if e % 2 == 0]
print(' '.join(arr))
