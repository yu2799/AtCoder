from collections import deque
from math import sqrt
from sys import stdin


def prime_factorization(n):
    prime_list = deque()
    if n % 2 == 0:
        n //= 2
        prime_list.append(2)
        if n % 2:
            prime_list.appendleft(int(sqrt(n)))
        else:
            prime_list.append(n // 2)
        return prime_list
    f = 3
    while f * f <= n:
        if n % f == 0:
            n //= f
            prime_list.append(f)
            if n % f:
                prime_list.appendleft(int(sqrt(n)))
            else:
                prime_list.append(n // f)
            return prime_list
        else:
            f += 2


def main():
    input = stdin.readline
    t = int(input())
    test = [int(input()) for _ in [0] * t]
    res = []
    for n in test:
        res.append(prime_factorization(n))
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
