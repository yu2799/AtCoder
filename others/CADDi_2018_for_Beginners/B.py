from sys import stdin


def main():
    input = stdin.readline
    n, h, w = map(int, input().split())
    res = 0
    for _ in [0] * n:
        a, b = map(int, input().split())
        if h <= a and w <= b:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
