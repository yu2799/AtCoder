from sys import stdin


def main():
    input = stdin.readline
    a = map(int, input().split())
    print("win" if sum(a) <= 21 else "bust")


if __name__ == "__main__":
    main()
