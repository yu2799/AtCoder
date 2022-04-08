n, k = map(int, input().split())
tmp = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i, j in zip(a, b):
    tmp += abs(i - j)

if k >= tmp and (k - tmp) % 2 == 0:
    print("Yes")
else:
    print("No")
