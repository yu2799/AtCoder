n = int(input())
p = [int(i) for i in input().split()]
cnt = 0
for i in range(n-2):
    a = p[i:i+3]
    if a[0] <= a[1] <= a[2] or a[0] >= a[1] >= a[2]:
        cnt += 1
print(cnt)