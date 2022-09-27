from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    idx = s.index("1")
    print("Takahashi" if idx % 2 == 0 else "Aoki")


if __name__ == "__main__":
    main()
