from sys import stdin


def main():
    input = stdin.readline
    n, _ = map(int, input().split())
    s = [input()[:-1] for _ in [0] * n]
    s.sort()
    print(*s, sep="")


if __name__ == "__main__":
    main()
