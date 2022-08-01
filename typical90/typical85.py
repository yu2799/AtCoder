from sys import stdin


def enumerate_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def main():
    input = stdin.readline
    k = int(input())
    res = 0
    d = enumerate_divisors(k)
    for i in range(len(d)):
        for j in range(i, len(d)):
            if k % (d[i] * d[j]) == 0 and k // d[i] // d[j] >= d[j]:
                res = res + 1
    print(res)


if __name__ == "__main__":
    main()
