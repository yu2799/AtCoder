from sys import stdin


def eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return {p for p, f in enumerate(sieve) if f}


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    prime_list = eratosthenes(200)
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            if (i + j) in prime_list:
                break
        else:
            print("Takahashi")
            return
    print("Aoki")


if __name__ == "__main__":
    main()
