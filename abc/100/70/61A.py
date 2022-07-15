from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    print("Yes" if a <= c <= b else "No")


if __name__ == "__main__":
    main()
