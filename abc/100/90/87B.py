a = int(input())
b = int(input())
c = int(input())
x = int(input())
res = 0
for i in range(a+1):
    for j in range(b+1):
        k = (x - i*500 - j*100) // 50
        if 0 <= k <= c:
            res += 1
print(res)
