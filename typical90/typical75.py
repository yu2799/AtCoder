from sys import stdin


def prime_factorize(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            cnt += 1
            n //= f
        else:
            f += 2
    if n != 1:
        cnt += 1
    return cnt


def main():
    input = stdin.readline
    n = int(input())
    cnt = prime_factorize(n)
    res = 0
    while 2 ** res < cnt:
        res += 1
    print(res)


if __name__ == '__main__':
    main()
