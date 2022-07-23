from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    res = []
    dist = [0] * (n + 1)
    tmp = 0
    for i in range(1, n + 2):
        dist[i - 1] = abs(a[i] - a[i - 1])
        tmp = tmp + dist[i - 1]
    for i in range(1, n + 1):
        res.append(tmp - dist[i - 1] - dist[i] + abs(a[i - 1] - a[i + 1]))
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
