n, a, b = map(int, input().split())
res = 0
for i in range(1, n+1):
    tmp = 0
    n = i
    while n > 0:
        tmp += n % 10
        n //= 10
    if a <= tmp <= b:
        res += i
print(res)
