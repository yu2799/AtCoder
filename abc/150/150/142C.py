from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    res = [0] * n
    for i, data in enumerate(a):
        res[data - 1] = i + 1
    print(*res)


if __name__ == "__main__":
    main()
