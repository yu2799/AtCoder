n = int(input())
a = list(map(int, input().split()))
res = 0
while True:
    for i in range(len(a)):
        if not a[i] % 2:
            a[i] //= 2
        else:
            print(res)
            exit()
    res += 1
