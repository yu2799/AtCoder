from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    res = [i for i in a if i % 2 == 0]
    print(*res)


if __name__ == "__main__":
    main()
