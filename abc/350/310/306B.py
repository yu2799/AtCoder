from sys import stdin


def main():
    input = stdin.readline
    a = input().split()
    print(int("".join(reversed(a)), 2))


if __name__ == "__main__":
    main()
