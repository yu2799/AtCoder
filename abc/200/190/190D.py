from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    while n % 2 == 0:
        n //= 2
    sq = int(n ** 0.5)
    cnt = sum([n % i == 0 for i in range(1, sq + 1)]) * 2 - (sq ** 2 == n)
    print(2 * cnt)


if __name__ == "__main__":
    main()
