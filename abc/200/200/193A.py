from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print((1 - b / a) * 100)


if __name__ == '__main__':
    main()
