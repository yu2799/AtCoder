a, b = map(int, input().split())
res = 1
cnt = 0
while res < b:
    res -= 1
    res += a
    cnt += 1
print(cnt)