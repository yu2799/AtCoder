from sys import stdin


def main():
    input = stdin.readline
    a, b, c = sorted(map(int, input().split()))
    print(c * 10 + b + a)


if __name__ == "__main__":
    main()
