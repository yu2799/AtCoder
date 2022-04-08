n = int(input())
a = [int(i) for i in input().split()]
res = 0
for i in a:
    if i > 10:
        res += (i - 10)
print(res)
