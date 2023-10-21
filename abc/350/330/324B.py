from sys import stdin


def prime_factorization(n):
    prime_list = []
    while n % 2 == 0:
        prime_list.append(2)
        n //= 2
    while n % 3 == 0:
        prime_list.append(3)
        n //= 3
    return n == 1


def main():
    input = stdin.readline
    n = int(input())
    print("Yes" if prime_factorization(n) else "No")


if __name__ == "__main__":
    main()
