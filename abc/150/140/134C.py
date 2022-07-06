from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(input()) for _ in [0] * n]
    first, second = sorted(a, reverse=True)[:2]
    res = [second if i == first else first for i in a]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
