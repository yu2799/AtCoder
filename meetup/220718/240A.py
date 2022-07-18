from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print("Yes" if (a + 1) == b or a == (b + 1) % 10 else "No")


if __name__ == "__main__":
    main()
