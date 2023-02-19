from sys import stdin


def main():
    input = stdin.readline
    a = list(sorted(map(int, input().split())))
    print(a[1])


if __name__ == "__main__":
    main()
