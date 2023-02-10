from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    if a != c:
        print("Takahashi" if a < c else "Aoki")
    else:
        print("Takahashi" if b <= d else "Aoki")


if __name__ == "__main__":
    main()
