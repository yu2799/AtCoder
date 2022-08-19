from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    print(pow(a, pow(b, c, 4) + 4, 10))


if __name__ == "__main__":
    main()
