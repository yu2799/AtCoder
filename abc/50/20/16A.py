from sys import stdin


def main():
    input = stdin.readline
    m, d = map(int, input().split())
    print("YES" if m % d == 0 else "NO")


if __name__ == "__main__":
    main()
