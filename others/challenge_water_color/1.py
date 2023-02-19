from sys import stdin


def main():
    input = stdin.readline
    while True:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            break
        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                k = x - i - j
                if j < k <= n:
                    res += 1
        print(res)


if __name__ == "__main__":
    main()
