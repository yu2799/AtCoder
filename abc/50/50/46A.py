from sys import stdin


def main():
    input = stdin.readline
    res = set(map(int, input().split()))
    print(len(res))


if __name__ == "__main__":
    main()
