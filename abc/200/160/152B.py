from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    a, b = str(a) * b, str(b) * a
    print(a if a < b else b)


if __name__ == "__main__":
    main()
