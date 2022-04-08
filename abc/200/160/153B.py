from sys import stdin


def main():
    input = stdin.readline
    h, n = map(int, input().split())
    a = [int(i) for i in input().split()]
    print("Yes" if sum(a) >= h else "No")


if __name__ == "__main__":
    main()
