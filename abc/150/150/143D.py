from bisect import bisect_left

n = int(input())
l = sorted([int(i) for i in input().split()])
res = 0
for i in range(n):
    for j in range(i+1, n):
        # a+bより小さい値のindexを二分探索，その後b以下を取り除く
        res += bisect_left(l, l[i]+l[j]) - (j+1) 
print(res)