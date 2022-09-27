from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    t = 0
    res = 0
    for a, b in ab:
        t += a / b
    t /= 2
    for a, b in ab:
        res += min(a, t * b)
        t -= min(a / b, t)
    print(res)


if __name__ == "__main__":
    main()
