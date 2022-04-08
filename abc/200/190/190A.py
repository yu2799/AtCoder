from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    if a == b:
        if c:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == "__main__":
    main()
