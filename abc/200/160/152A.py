from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    print("Yes" if n == m else "No")


if __name__ == "__main__":
    main()
