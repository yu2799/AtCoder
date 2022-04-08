n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
res = 0
for i in range(n):
    if a[i] >= b[i]:
        res += b[i]
    elif a[i] < b[i] <= a[i] + a[i+1]:
        a[i+1] = a[i+1]-(b[i]-a[i])
        res += b[i]
    else:
        res += a[i] + a[i+1]
        a[i+1] = 0
print(res)