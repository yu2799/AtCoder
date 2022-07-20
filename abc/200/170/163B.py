from sys import stdin


def main():
    input = stdin.readline
    n, _ = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = sum(a)
    print(n - tmp if n - tmp >= 0 else -1)


if __name__ == "__main__":
    main()
