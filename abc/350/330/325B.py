from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    wx = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(24):
        tmp = 0
        for w, x in wx:
            if 9 <= (i + x) % 24 < 18:
                tmp += w
        res = max(tmp, res)
    print(res)


if __name__ == "__main__":
    main()
