from sys import stdin


def main():
    input = stdin.readline
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = [False] * (w + 1)
    l = len(a)
    for i in range(l):
        if a[i] <= w:
            res[a[i]] = True
        for j in range(i + 1, l):
            if a[i] + a[j] <= w:
                res[a[i] + a[j]] = True
            for k in range(j + 1, l):
                if a[i] + a[j] + a[k] <= w:
                    res[a[i] + a[j] + a[k]] = True

    print(sum(res))


if __name__ == '__main__':
    main()
