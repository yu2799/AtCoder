from sys import stdin


def main():
    input = stdin.readline
    n, p, q = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n-4):
        tmpI = a[i] % p
        for j in range(i+1, n-3):
            tmpJ = a[j] * tmpI % p
            for k in range(j+1, n-2):
                tmpK = a[k] * tmpJ % p
                for l in range(k+1, n-1):
                    tmpL = a[l] * tmpK % p
                    for m in range(l+1, n):
                        tmpM = a[m] * tmpL % p
                        if tmpM == q:
                            res += 1
    print(res)


if __name__ == '__main__':
    main()
