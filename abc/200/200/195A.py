from sys import stdin


def main():
    input = stdin.readline
    m, h = map(int, input().split())
    print("Yes" if h % m == 0 else "No")


if __name__ == "__main__":
    main()
