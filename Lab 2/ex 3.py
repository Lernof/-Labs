import sys
a = int(input())
for e in range(1,a+1):
    if a % e == 0:
        sys.stdout.write(str(e) + ' ')
