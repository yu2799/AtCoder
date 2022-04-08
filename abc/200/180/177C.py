n = int(input())
a = list(map(int, input().split()))
r_sum = sum(a)
res = 0
for i in range(1, n):
    r_sum -= a[i]
    res += r_sum * a[i]
print(res % (10 ** 9 + 7))
