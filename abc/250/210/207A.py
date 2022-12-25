from sys import stdin


def main():
    input = stdin.readline
    _, b, c = sorted(map(int, input().split()))
    print(b + c)


if __name__ == "__main__":
    main()
