from sys import stdin


def main():
    input = stdin.readline
    a, b = sorted(map(int, input().split()))
    print("Yes" if a * 2 == b or a * 2 + 1 == b else "No")


if __name__ == "__main__":
    main()
