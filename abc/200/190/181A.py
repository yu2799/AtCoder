from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print("White" if n % 2 == 0 else "Black")


if __name__ == "__main__":
    main()
