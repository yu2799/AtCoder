from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [input()[:-1] for _ in [0] * n]
    b = [input()[:-1] for _ in [0] * m]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            tmp = [a[i + k][j : j + m] for k in range(m)]
            if tmp == b:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
