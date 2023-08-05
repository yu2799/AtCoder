from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        x[i] = a + b
        y[i] = a - b
    x.sort()
    y.sort()
    print(max(x[-1] - x[0], y[-1] - y[0]))


if __name__ == "__main__":
    main()
