from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(input()) for _ in range(n)]
    f, s = sorted(a, reverse=True)[:2]
    print(*[f if i != f else s for i in a], sep="\n")


if __name__ == "__main__":
    main()
