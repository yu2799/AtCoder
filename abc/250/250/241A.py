from sys import stdin


def main():
    input = stdin.readline
    a = list(map(int, input().split()))
    print(a[a[a[0]]])


if __name__ == "__main__":
    main()
