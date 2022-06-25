from sys import stdin


def main():
    input = stdin.readline
    a, b, n = map(int, input().split())
    tmp = min(b - 1, n)
    print(a * tmp // b)


if __name__ == "__main__":
    main()
