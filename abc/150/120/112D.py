from sys import stdin


def enumerate_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    for i in enumerate_divisors(m):
        tmp = m // i
        if n <= tmp:
            print(i)
            return
    print(1)


if __name__ == "__main__":
    main()
