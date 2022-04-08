n = int(input())
a = [int(i) for i in input().split()]
cnt = 1
d = 0
for i in a:
    if i == cnt:
        cnt += 1
    else:
        d += 1
if d == len(a):
    print(-1)
else:
    print(d)
