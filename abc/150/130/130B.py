n, x = map(int, input().split())
l = [int(i) for i in input().split()]
cnt = 1
tmp = 0
for i in l:
    tmp += i
    if tmp > x:
        print(cnt)
        exit(0)
    cnt += 1
print(cnt)