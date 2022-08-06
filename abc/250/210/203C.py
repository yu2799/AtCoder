from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    ab.sort()
    res = 0
    prev = 0
    for a, b in ab:
        if k - (a - prev) >= 0:
            k = k - (a - prev) + b
            res = res + a - prev
            prev = a
        else:
            break
    print(res + k)


if __name__ == "__main__":
    main()
