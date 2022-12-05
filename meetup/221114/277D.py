from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
        d[i + m] += 1
    d = sorted(d.items())
    accm = [0] * (len(d) + 1)
    for i in range(len(d)):
        accm[i + 1] = accm[i] + (d[i][0] % m) * d[i][1]
    res = 0
    prev = -1
    left = 0
    for i in range(len(d)):
        num, _ = d[i]
        if prev + 1 != num:
            if accm[i] - accm[left] > res:
                res = accm[i] - accm[left]
            left = i
        prev = num
    if left == 0:
        print(0)
        return
    elif accm[-1] - accm[left] > res:
        res = accm[-1] - accm[left]
    print(accm[-1] // 2 - res)


if __name__ == "__main__":
    main()
