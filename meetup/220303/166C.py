from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    h = [int(i) for i in input().split()]
    res = [True] * n
    for _ in [0] * m:
        a, b = [int(i) - 1 for i in input().split()]
        if h[a] > h[b]:
            res[b] = False
        elif h[a] < h[b]:
            res[a] = False
        else:
            res[a] = False
            res[b] = False
    print(sum(res))


if __name__ == "__main__":
    main()
