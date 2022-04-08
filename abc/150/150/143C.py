n = int(input())
s = input()
res = 1
prev = s[0]
for i in range(1, n):
    if prev != s[i]:
        res += 1
        prev = s[i]
print(res)