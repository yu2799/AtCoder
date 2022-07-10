from sys import stdin


def main():
    input = stdin.readline
    p, q, r = sorted(map(int, input().split()))
    print(p + q)


if __name__ == "__main__":
    main()
