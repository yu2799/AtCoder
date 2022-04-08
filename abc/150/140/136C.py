n = int(input())
h = [int(i) for i in input().split()]
pre = h[0]
for i in h:
    if pre > i:
        print("No")
        exit()
    elif pre < i:
        pre = i - 1
print("Yes")