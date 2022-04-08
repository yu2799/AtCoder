from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    if -(2 ** 31) <= n < 2 ** 31:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
