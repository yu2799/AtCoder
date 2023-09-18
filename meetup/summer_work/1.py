from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n - 1):
        res += abs(xy[i][0] - xy[i + 1][0]) + abs(xy[i][1] - xy[i + 1][1])
    print(res)


if __name__ == "__main__":
    main()
