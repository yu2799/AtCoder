from sys import stdin


def main():
    input = stdin.readline
    n, t = map(int, input().split())
    ct = [tuple(map(int, input().split())) for _ in [0] * n]
    res = 1001
    for i in ct:
        if i[1] <= t and i[0] < res:
            res = i[0]
    print(res if res <= 1000 else "TLE")


if __name__ == "__main__":
    main()
