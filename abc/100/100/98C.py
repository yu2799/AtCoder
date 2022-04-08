n = int(input())
s = input()
tmp = s[1:].count("E")
res = tmp
for i in range(1, n):
    if s[i-1] == "W":
        tmp += 1
    if s[i] == "E":
        tmp -= 1
    if tmp < res:
        res = tmp

print(res)
