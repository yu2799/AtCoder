s = input()
res = 0
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        res += 1
print(res)