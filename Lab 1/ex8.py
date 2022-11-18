a = int(input())
b = int(input())
c = int(input())
if a < c + b and b < a + c and c < a + b:
    print('YES')
else:print('NO')
