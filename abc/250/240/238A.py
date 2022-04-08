from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    if n == 1 or 5 <= n:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
