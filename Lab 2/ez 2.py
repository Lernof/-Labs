def der(a:int) -> int:
    for e in range(2,a + 1):
        if a % e == 0:
            return e
        
print(der(int(input())))
