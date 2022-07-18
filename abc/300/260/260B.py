from sys import stdin


def main():
    input = stdin.readline
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = []
    for i in range(n):
        ab.append((a[i], -i, b[i]))
    ab.sort(reverse=True)
    res = []
    cnt = 0
    while cnt < x:
        res.append(-ab[cnt][1] + 1)
        cnt += 1
    ab = []
    for i in range(n):
        ab.append((b[i], -i, a[i]))
    ab.sort(reverse=True)
    cnt = 0
    i = 0
    while cnt < y:
        tmp = -ab[i][1] + 1
        if tmp not in res:
            res.append(tmp)
            cnt += 1
        i += 1
    tmp = [(a[i] + b[i], -i) for i in range(n)]
    tmp.sort(reverse=True)
    cnt = 0
    i = 0
    while cnt < z:
        aaa = -tmp[i][1] + 1
        if aaa not in res:
            res.append(aaa)
            cnt += 1
        i += 1
    res.sort()
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
