from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    print(sum(a))


if __name__ == "__main__":
    main()
