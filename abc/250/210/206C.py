n = int(input())
a = sorted([int(i) for i in input().split()])
l = len(a)
prev = a[0]
cnt = 0
res = 0
for i in a:
    if prev == i:
        cnt += 1
    else:
        l -= cnt
        res += l * cnt
        cnt = 1
        prev = i
print(res)
