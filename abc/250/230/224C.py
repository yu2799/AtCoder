from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    res = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (xy[j][0] - xy[i][0]) * (xy[k][1] - xy[i][1]) == (
                    xy[k][0] - xy[i][0]
                ) * (xy[j][1] - xy[i][1]):
                    continue
                res += 1
    print(res)


if __name__ == "__main__":
    main()
