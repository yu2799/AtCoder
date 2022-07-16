from sys import stdin


def main():
    input = stdin.readline
    a, b, c = sorted(map(int, input().split()))
    print(a if a != b else c)


if __name__ == "__main__":
    main()
