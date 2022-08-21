from sys import stdin


def main():
    input = stdin.readline
    a, b = map(str, input().split())
    a = sum([int(i) for i in a])
    b = sum([int(i) for i in b])
    print(b if a < b else a)


if __name__ == "__main__":
    main()
