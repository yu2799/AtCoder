from sys import stdin


def main():
    input = stdin.readline
    n, m = sorted(map(int, input().split()))
    if n == 1:
        if m == 1:
            print(1)
        else:
            print(m - 2)
    elif n == 2:
        print(0)
    else:
        print(n * m - 2 * (n + m) + 4)


if __name__ == "__main__":
    main()
