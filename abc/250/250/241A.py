from sys import stdin


def main():
    input = stdin.readline
    a = [int(i) for i in input().split()]
    print(a[a[a[0]]])


if __name__ == "__main__":
    main()
