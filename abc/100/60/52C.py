from sys import stdin
from collections import defaultdict


def prime_factorization(n):
    prime_list = []
    while n % 2 == 0:
        prime_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_list.append(n)
    return prime_list


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(int)
    res = 1
    MOD = 10**9 + 7
    for i in range(2, n + 1):
        for j in prime_factorization(i):
            d[j] += 1

    for i in d.values():
        res *= i + 1
        res %= MOD
    print(res)


if __name__ == "__main__":
    main()
