from sys import stdin


def main():
    input = stdin.readline
    a = int(input())
    s = input()[:-1]
    print("red" if a < 3200 else s)


if __name__ == "__main__":
    main()
