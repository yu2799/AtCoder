from itertools import accumulate

n = int(input())
s1, s2 = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    c, p = map(int, input().split())
    if c == 1:
        s1[i] = p
    else:
        s2[i] = p

    # 累積和計算
    # if c == 1:
    #     s1[i] = s1[i-1] + p
    #     s2[i] = s2[i-1]
    # else:
    #     s2[i] = s2[i-1] + p
    #     s1[i] = s1[i-1]
s1, s2 = list(accumulate(s1)), list(accumulate(s2))

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(s1[r]-s1[l-1], s2[r]-s2[l-1])
