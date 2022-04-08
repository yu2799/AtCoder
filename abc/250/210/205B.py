n = int(input())
a = sorted([int(i) for i in input().split()])
for i in range(len(a)):
    if (i+1) != a[i]:
        print("No")
        exit()
print("Yes")
