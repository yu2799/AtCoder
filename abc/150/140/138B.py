from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / i for i in a]))


if __name__ == "__main__":
    main()
