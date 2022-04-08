from sys import stdin


def main():
    input = stdin.readline
    n, w = map(int, input().split())
    ab = []
    for _ in [0] * n:
        ab.append(list(map(int, input().split())))
    ab.sort(reverse=True)

    res = 0
    tmp = 0
    for a, b in ab:
        res += a * b
        tmp += b
        if tmp >= w:
            res -= (tmp - w) * a
            break
    print(res)


if __name__ == "__main__":
    main()
