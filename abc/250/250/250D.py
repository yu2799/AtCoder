from sys import stdin
from itertools import accumulate


def eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p, f in enumerate(sieve) if f]


def main():
    input = stdin.readline
    n = int(input())
    primes = eratosthenes(10 ** 6)
    tmp = [0] * (10 ** 6 + 1)
    for i in primes:
        tmp[i] += 1
    accm = list(accumulate(tmp))
    res = 0
    for i in primes:
        tmp = min(n // i // i // i, i-1)
        res += accm[tmp]
    print(res)


if __name__ == '__main__':
    main()
