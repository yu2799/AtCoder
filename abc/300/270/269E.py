n = int(input())
a, b, c, d = 1, n, 1, n
while a != b:
    mid = (a + b) // 2
    print("?", a, mid, 1, n)
    t = int(input())
    if t == mid - a + 1:
        a = mid + 1
    else:
        b = mid
while c != d:
    mid = (c + d) // 2
    print("?", 1, n, c, mid)
    t = int(input())
    if t == mid - c + 1:
        c = mid + 1
    else:
        d = mid
print("!", a, c)
