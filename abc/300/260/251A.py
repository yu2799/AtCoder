from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    l = len(s)
    if l == 1:
        print(s * 6)
    elif l == 2:
        print(s * 3)
    else:
        print(s * 2)


if __name__ == '__main__':
    main()
