from sys import stdin


def main():
    input = stdin.readline
    x = list(map(int, input().split()))
    print("YES" if x.count(5) == 2 and x.count(7) == 1 else "NO")


if __name__ == "__main__":
    main()
