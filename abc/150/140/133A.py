from sys import stdin


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    print(n * a if n * a < b else b)


if __name__ == "__main__":
    main()
