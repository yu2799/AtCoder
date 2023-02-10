from math import gcd
from sys import stdin


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


def bit_exhaustive_seach(product_list):
    n = len(product_list)
    res = []
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i >> j & 1:
                tmp.append(product_list[j])
        res.append(tmp)
    return res


def main():
    input = stdin.readline
    _ = int(input())
    x = list(map(int, input().split()))
    res = []
    d = set()
    for i in x:
        for j in prime_factorization(i):
            d.add(j)
    for i in bit_exhaustive_seach(list(d)):
        if not i:
            continue
        tmp = 1
        for j in i:
            tmp *= j
        for j in x:
            if gcd(tmp, j) == 1:
                break
        res.append(tmp)
    print(min(res))


if __name__ == "__main__":
    main()
