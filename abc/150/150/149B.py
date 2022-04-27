from sys import stdin


def main():
    input = stdin.readline
    a, b, k = map(int, input().split())
    if a - k >= 0:
        print(a-k, b)
    else:
        print(0, max(0, b - (k - a)))


if __name__ == '__main__':
    main()