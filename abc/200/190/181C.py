from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (xy[i][1] - xy[j][1]) * (xy[i][0] - xy[k][0]) == (
                    xy[i][0] - xy[j][0]
                ) * (xy[i][1] - xy[k][1]):
                    print("Yes")
                    return
    print("No")


if __name__ == "__main__":
    main()
