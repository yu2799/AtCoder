from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    res = []
    for _ in [0] * q:
        (*query,) = map(int, input().split())
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        else:
            res.append(a[query[1] - 1])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
