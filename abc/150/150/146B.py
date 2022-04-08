n = int(input())
s = input()
res = []
buf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in s:
    res.append(buf[(buf.index(i)+n)%26])
print("".join(res))