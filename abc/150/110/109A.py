from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print("Yes" if a * b % 2 else "No")


if __name__ == "__main__":
    main()
