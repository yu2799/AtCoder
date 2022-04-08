n = int(input())
d = sorted([int(i) for i in input().split()])
if d[n//2] != d[n//2-1]:
    print(d[n//2]-d[n//2-1])
else:
    print(0)
