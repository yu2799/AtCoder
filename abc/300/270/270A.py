from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    c = a | b
    print(c)


if __name__ == "__main__":
    main()
