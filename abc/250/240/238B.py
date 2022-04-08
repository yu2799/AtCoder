from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    deg = [False] * 360
    deg[0] = True
    tmp = 0
    for i in a:
        tmp += i
        deg[tmp % 360] = True
    l = 0
    res = 0
    for r in range(360):
        if deg[r]:
            if r - l > res:
                res = r - l
            l = r
    print(max(res, r + 1 - l))


if __name__ == "__main__":
    main()
