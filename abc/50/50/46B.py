from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    print(k * pow(k - 1, n - 1))


if __name__ == "__main__":
    main()
