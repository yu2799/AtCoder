from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print("Yes" if -pow(2, 31) <= n < pow(2, 31) else "No")


if __name__ == "__main__":
    main()
