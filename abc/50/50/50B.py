from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    t = list(map(int, input().split()))
    t_sum = sum(t)
    m = int(input())
    res = []
    for _ in [0] * m:
        p, x = map(int, input().split())
        res.append(t_sum - t[p - 1] + x)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
