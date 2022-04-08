n = int(input())
a = [int(i) for i in input().split()]
res = 0
for i in a:
    res += 1 / i
print(1 / res)