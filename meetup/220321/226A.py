from sys import stdin


def main():
    input = stdin.readline
    a, b = input().split(".")
    print(int(a) + (1 if int(b[0]) >= 5 else 0))


if __name__ == "__main__":
    main()
