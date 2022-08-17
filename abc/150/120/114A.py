from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    print("YES" if x == 3 or x == 5 or x == 7 else "NO")


if __name__ == "__main__":
    main()
