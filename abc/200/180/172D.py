from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    r = int(n**0.5)

    print(
        sum(k * (n // k) * (n // k + 1) for k in range(1, r + 1))
        - (r * (r + 1) // 2) ** 2
    )


if __name__ == "__main__":
    main()
