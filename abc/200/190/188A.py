from sys import stdin


def main():
    input = stdin.readline
    x, y = sorted(map(int, input().split()))
    print("Yes" if x + 3 > y else "No")


if __name__ == "__main__":
    main()
