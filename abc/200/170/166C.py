from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    res = [1] * n
    for _ in [0] * m:
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        if h[b] < h[a]:
            res[b] = 0
        elif h[b] > h[a]:
            res[a] = 0
        else:
            res[a], res[b] = 0, 0

    print(res.count(1))


if __name__ == '__main__':
    main()
