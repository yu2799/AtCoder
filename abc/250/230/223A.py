from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    print("Yes" if x % 100 == 0 and x != 0 else "No")


if __name__ == "__main__":
    main()
