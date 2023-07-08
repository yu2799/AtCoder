from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    tmp = n % 5
    print(n + (5 - tmp) if abs(5 - tmp) < tmp else n - tmp)


if __name__ == "__main__":
    main()
