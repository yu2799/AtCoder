from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    print("YES" if b - a == c - b else "NO")


if __name__ == "__main__":
    main()
