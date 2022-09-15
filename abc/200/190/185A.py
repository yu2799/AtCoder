from sys import stdin


def main():
    input = stdin.readline
    a = sorted(map(int, input().split()))
    print(a[0])


if __name__ == "__main__":
    main()
