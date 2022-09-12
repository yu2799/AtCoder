from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    if a * d == b * c:
        print("DRAW")
    elif a * d < b * c:
        print("TAKAHASHI")
    else:
        print("AOKI")


if __name__ == "__main__":
    main()
