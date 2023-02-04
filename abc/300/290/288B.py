from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    s = [input()[:-1] for _ in range(n)]
    res = sorted(s[:k])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
