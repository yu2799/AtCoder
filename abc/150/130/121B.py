from sys import stdin


def main():
    input = stdin.readline
    n, _, c = map(int, input().split())
    b = list(map(int, input().split()))
    res = 0
    for _ in [0] * n:
        a = list(map(int, input().split()))
        if sum([i * j for i, j in zip(a, b)]) + c > 0:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
