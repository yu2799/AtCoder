from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print("YES" if n % 3 == 0 else "NO")


if __name__ == "__main__":
    main()
