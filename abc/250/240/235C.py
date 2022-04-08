from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    d = {0: []}
    res = []
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]].append(i+1)
        else:
            d[a[i]] = []
            d[a[i]].append(i+1)
    for _ in [0] * q:
        x, k = map(int, input().split())
        if x in d and k <= len(d[x]):
            res.append(d[x][k-1])
        else:
            res.append(-1)
    print(*res, sep="\n")


if __name__ == '__main__':
    main()
