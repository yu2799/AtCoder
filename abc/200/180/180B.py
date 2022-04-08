n = int(input())
x = [int(i) for i in input().split()]
res = 0
m = 0
for i in x:
    res += abs(i)
    if m < abs(i):
        m = abs(i)
print(res)
res = 0
for i in x:
    res += i * i
print(pow(res, 0.5))
print(m)