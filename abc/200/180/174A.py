from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    print("Yes" if x >= 30 else "No")


if __name__ == "__main__":
    main()
