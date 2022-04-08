n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
res = 0
prev = n+1
for i in range(n):
    res += b[a[i]-1]
    if prev == a[i]-1:
        res += c[prev-1]
    prev = a[i]
print(res)