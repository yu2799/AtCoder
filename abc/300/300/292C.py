from sys import stdin


def enumerate_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    return divisors


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for ab in range(1, n):
        cd = n - ab
        res += enumerate_divisors(ab) * enumerate_divisors(cd)
    print(res)


if __name__ == "__main__":
    main()
