from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    res = [True] * n
    for _ in [0] * k:
        _ = int(input())
        tmp = [int(i) - 1 for i in input().split()]
        for i in tmp:
            res[i] = False
    print(sum(res))


if __name__ == "__main__":
    main()
