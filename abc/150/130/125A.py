from sys import stdin


def main():
    input = stdin.readline
    a, b, t = map(int, input().split())
    print(t // a * b)


if __name__ == '__main__':
    main()