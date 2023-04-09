def dfs(x, y):
    global res
    global tmp
    tmp.add(a[y][x])
    if len(tmp) != x + y + 1:
        return
    if y < h - 1:
        dfs(x, y + 1)
    if x < w - 1:
        dfs(x + 1, y)
    if y == h - 1 and x == w - 1:
        res += 1
    tmp.remove(a[y][x])


h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
res = 0
tmp = set()
dfs(0, 0)
print(res)
