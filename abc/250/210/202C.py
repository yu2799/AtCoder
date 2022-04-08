from collections import Counter

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

dict_a = Counter(a)
dict_c = Counter(c)
res = 0
for i, j in zip(dict_c.keys(), dict_c.values()):
    res += dict_a[b[i - 1]] * j
print(res)
