from sys import stdin
from itertools import accumulate


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    else:
        l = int(pow(n, 0.5)) + 1
        for i in range(3, l, 2):
            if n % i == 0:
                return False
        else:
            return True


def main():
    input = stdin.readline
    q = int(input())
    res = []
    tmp = [0] * (10 ** 5 + 1)
    for i in range(1, 10 ** 5 + 1, 2):
        if is_prime(i) and is_prime((i + 1) // 2):
            tmp[i] = 1
    accm = list(accumulate(tmp))
    for _ in [0] * q:
        l, r = map(int, input().split())
        res.append(accm[r] - accm[l - 1])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
