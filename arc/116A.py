t = int(input())
for i in range(t):
    n = int(input())
    if n % 4 == 0:
        print("Even")
    elif n % 2 == 0:
        print("Same")
    else:
        print("Odd")