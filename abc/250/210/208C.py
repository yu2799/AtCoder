from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = k // n
    mid = sorted(a)[k % n]
    res = [tmp + 1 if i < mid else tmp for i in a]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
