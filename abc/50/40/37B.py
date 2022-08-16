from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    res = [0] * n
    for _ in [0] * q:
        left, right, t = map(int, input().split())
        for i in range(left - 1, right):
            res[i] = t
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
