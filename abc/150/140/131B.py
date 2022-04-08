n, l = map(int, input().split())
tmp = (l-1)*n + (n+1)*n//2
if l+n-1 <= 0:
    print(tmp - (l+n-1))
elif l >= 0:
    print(tmp - l)
else:
    print(tmp)