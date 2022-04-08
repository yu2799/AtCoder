from sys import stdin


def main():
    input = stdin.readline
    n, x, y = map(int, input().split())
    res = [0] * n
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            d = min(j - i, abs(x - i) + abs(y - j) + 1)
            res[d] += 1
    print(*(res[1:]), sep="\n")


if __name__ == "__main__":
    main()
