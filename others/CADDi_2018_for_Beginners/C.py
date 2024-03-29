from collections import defaultdict
from sys import stdin


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
    n, p = map(int, input().split())
    res = 1
    for i, j in prime_factorization(p).items():
        if j // n > 0:
            res = res * (pow(i, j // n))
    print(res)


if __name__ == "__main__":
    main()
