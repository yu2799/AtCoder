a, b, c = map(int, input().split())
if a == b:
    print("=")
elif abs(a) == abs(b):
    if c % 2 == 0:
        print("=")
    else:
        if a > b:
            print(">")
        else:
            print("<")
elif a >= 0 and b >= 0:
    if a > b:
        print(">")
    else:
        print("<")
elif a <= 0 and b <= 0:
    if abs(a) > abs(b):
        if c % 2 == 0:
            print(">")
        else:
            print("<")
    else:
        if c % 2 == 0:
            print("<")
        else:
            print(">")
elif a >= 0 and b <= 0:
    if a > abs(b):
        print(">")
    else:
        if c % 2 == 0:
            print("<")
        else:
            print(">")
else:
    if abs(a) < b:
        print("<")
    else:
        if c % 2 == 0:
            print(">")
        else:
            print("<")
