n = int(input())
res = 0
cnt = 1
while res < n:
    res += cnt
    cnt += 1
print(cnt-1)
