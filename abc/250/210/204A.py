from sys import stdin


def main():
    input = stdin.readline
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        if x + y == 1:
            print(2)
        elif x + y == 2:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
