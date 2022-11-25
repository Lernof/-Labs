def clc(x: int, y:int, z:int) -> int:
    arr = [x,y,z]
    if arr.count(0) > arr.count(1):
        return 0
    else: return 1
arr = [int(e) for e in input().split()]
print(clc(*arr))
