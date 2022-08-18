from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n // 2] - d[n // 2 - 1])


if __name__ == "__main__":
    main()
