from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    s = input()[:-1]
    cnt = 0
    res = []
    for _ in [0] * q:
        t, x = map(int, input().split())
        if t == 1:
            cnt += x
            cnt %= n
        else:
            res.append(s[(x - cnt - 1) % n])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
