a, b, c, d = map(int, input().split())
if a <= c <= b:
    if d <= b:
        print(d-c)
    else:
        print(b-c)
elif c <= a <= d:
    if b <= d:
        print(b-a)
    else:
        print(d-a)
else:
    print(0)
