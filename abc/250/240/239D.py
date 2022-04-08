from sys import stdin


def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False

    return primes


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    l = list_primes(200)
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            if i + j in l:
                break
        else:
            print("Takahashi")
            exit()
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
