n = int(input())
a = 1
b = 1
if n < 8 or n % 2 != 0:
    print("-1")
    exit()
else:
    while 3**a + 5**b < n:
        wa = n - 5**b
        while wa > 3**a:
            a += 1
        if wa == 3**a:
            break
        a = 1
        b += 1
        
if 3**a + 5**b == n:
    print(a, b)
else:
    print("-1")