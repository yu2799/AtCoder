from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    mod = x % 11
    if mod == 0:
        print(x // 11 * 2)
    elif mod < 7:
        print(x // 11 * 2 + 1)
    else:
        print(x // 11 * 2 + 2)


if __name__ == '__main__':
    main()
