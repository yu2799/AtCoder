l, r = map(int, input().split())
res = 10**10
if r - l >= 2019:
    res = 0
else:
    for i in range(l, r):
        for j in range(i+1, r+1):
            res = min(res, i*j%2019)
            if res == 0:
                print(res)
                exit()
print(res)