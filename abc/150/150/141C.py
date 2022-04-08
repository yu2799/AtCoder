n, k, q = map(int, input().split())
p = [0] * n
for i in range(q):
    p[int(input())-1] += 1
for i in p:
    if k - q + i > 0:
        print("Yes")
    else:
        print("No")