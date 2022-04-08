from collections import Counter

n = int(input())
s = ["".join(sorted(input())) for _ in range(n)]
c = Counter(s)
res = 0
for i in c.keys():
    res += c[i]*(c[i]-1) // 2 # c[i]個中の2個取るコンビネーションの計算
print(res)