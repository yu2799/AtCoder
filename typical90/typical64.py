from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    a = [i for i in map(int, input().split())]
    b = [0] * (n-1)
    tmp = 0
    for i in range(n-1):
        b[i] = a[i+1] - a[i]
        tmp += abs(b[i])

    res = []
    for _ in [0] * q:
        l, r, v = map(int, input().split())
        l -= 1
        r -= 1
        if l > 0:
            tmp -= abs(b[l-1])
            b[l-1] += v
            tmp += abs(b[l-1])
        if r < n - 1:
            tmp -= abs(b[r])
            b[r] -= v
            tmp += abs(b[r])
        res.append(tmp)

    print(*res, sep="\n")


if __name__ == '__main__':
    main()
