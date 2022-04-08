n = int(input())
s = set()
res = []
for i in range(n):
    buf = input()
    if buf not in s:
        s.add(buf)
        res.append(i+1)
print(*res, sep="\n")
# 毎回出力よりこっちのほうが高速っぽい
# *はlistの[]を取って出力してくれる
