from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    x.sort()
    y.sort()
    x_center = x[n // 2]
    y_center = y[n // 2]
    res = 0
    for i, j in zip(x, y):
        res = res + abs(i - x_center) + abs(j - y_center)
    print(res)


if __name__ == "__main__":
    main()
