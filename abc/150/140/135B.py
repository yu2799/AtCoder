n = int(input())
p = [int(i) for i in input().split()]
ans = sorted(p)
cnt = 0
for i in range(n):
    if p[i] != ans[i]:
        cnt += 1    
if cnt >= 3:
    print("NO")
else:
    print("YES")