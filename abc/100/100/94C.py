from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    x = list(map(int, input().split()))
    left, right = sorted(x)[n // 2 - 1 : n // 2 + 1]
    res = []
    for i in x:
        if i < right:
            res.append(right)
        else:
            res.append(left)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
