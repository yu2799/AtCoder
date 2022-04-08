b, c = map(int, input().split())
if b > 0:
    if c <=2:
        print(c+1)
    else:
        print((c-2)*2+3-max(0, c-b*2))
else:
    print(abs(b)*2+c)