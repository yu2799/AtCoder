n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(a)
first = b[-1]
second = b[-2]
for i in a:
    if i == first:
        print(second)
    else:
        print(first)