from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    if x < 600:
        print(8)
    elif x < 800:
        print(7)
    elif x < 1000:
        print(6)
    elif x < 1200:
        print(5)
    elif x < 1400:
        print(4)
    elif x < 1600:
        print(3)
    elif x < 1800:
        print(2)
    else:
        print(1)


if __name__ == "__main__":
    main()
