from sys import stdin


def f(n):
    if n == 0:
        return 1
    return n * f(n - 1)


def main():
    input = stdin.readline
    n = int(input())
    print(f(n))


if __name__ == "__main__":
    main()
