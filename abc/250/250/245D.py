from sys import stdin


def main():
    input = stdin.readline
    _ = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.reverse()
    c.reverse()
    res = []
    cnt = 0
    a_l = len(a)
    c_l = len(c)
    while cnt + a_l <= c_l:
        tmp = c[cnt] // a[0]
        res.append(tmp)
        for i in range(1, a_l):
            c[cnt + i] -= tmp * a[i]
        cnt += 1
    res.reverse()
    print(*res)


if __name__ == "__main__":
    main()
