from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    if a <= c <= d <= b:
        print(d-c)
    elif a <= c <= b:
        print(b - c)
    elif c <= a <= b <= d:
        print(b - a)
    elif c <= a <= d:
        print(d - a)
    else:
        print(0)


if __name__ == '__main__':
    main()
