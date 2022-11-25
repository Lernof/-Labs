from math import pow
def culc(arr: list) -> int:    
    return pow(*[arr[0],arr[1]])
arr = [float(e) for e in input().split()]
print(culc(arr))
