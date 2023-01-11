from collections import defaultdict
from sys import stdin


def prime_factorization(n):
    prime_list = defaultdict(int)
    while not n & 1:
        prime_list[2] += 1
        n >>= 1
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
    k = int(input())
    res = 0
    for key, value in prime_factorization(k).items():
        for i in range(key, k + 1, key):
            j = i
            while value > 0 and j % key == 0:
                value -= 1
                j /= key
            if value == 0:
                if res < i:
                    res = i
                break
    print(res)


if __name__ == "__main__":
    main()
