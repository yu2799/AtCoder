def bin(a, b, x):
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        c = (r+l) // 2
        if isOk(a, b, x, c):
            l = c
        else:
            r = c
    return l

def isOk(a, b, x, c):
    if a*c + b*len(str(c)) <= x:
        return True
    else:
        return False

a, b, x = map(int, input().split())
print(bin(a, b, x))