from collections import defaultdict
from sys import stdin
from math import gcd


def prime_factorization(n):
    prime_list = defaultdict(int)
    while n % 2 == 0:
        prime_list[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_list[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        prime_list[n] += 1
    return prime_list


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(len(prime_factorization(gcd(a, b))) + 1)


if __name__ == "__main__":
    main()
