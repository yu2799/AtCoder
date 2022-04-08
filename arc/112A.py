t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    if (l == r and l != 0) or r < l*2:
        print(0)
    else:
        print((r-l*2+1)*(r-l*2+2)//2)