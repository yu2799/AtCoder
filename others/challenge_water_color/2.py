from sys import stdin


def enumerate_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for i in range(1, n + 1, 2):
        if len(enumerate_divisors(i)) == 8:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
