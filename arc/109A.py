a, b, x, y = map(int, input().split())
if a <= b:
    if 2*x <= y:
        print((b-a)*2*x+x)
    else:
        print(x+(b-a)*y)

elif a > b:
    if 2*x <= y:
        print((((a-b)*2)-1)*x)
    else:
        print((a-b-1)*y+x)