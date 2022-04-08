n = int(input())
a = [int(i) for i in input().split()]
cnt = [0] * (10**5 + 1)
res = 0
for i in a:
    cnt[i] += 1
    res += i
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    res = res + cnt[b]*(c-b)
    cnt[c] += cnt[b]
    cnt[b] = 0
    print(res)