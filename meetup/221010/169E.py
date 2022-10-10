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
    if n % 2:
        a = y[n // 2]
        b = x[n // 2]
    else:
        a = y[n // 2] + y[n // 2 - 1]
        b = x[n // 2] + x[n // 2 - 1]
    print(a - b + 1)


if __name__ == "__main__":
    main()
