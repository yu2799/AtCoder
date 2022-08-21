from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(sum([n / (n - i) for i in range(1, n)]))


if __name__ == "__main__":
    main()
