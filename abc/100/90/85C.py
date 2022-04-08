from sys import stdin


def main():
    input = stdin.readline
    n, y = map(int, input().split())
    for i in range(n+1):
        for j in range(n+1-i):
            k = n - i - j
            if k >= 0 and 10000*i + 5000*j + 1000*k == y:
                print(i, j, k)
                exit()
    print(-1, -1, -1)


if __name__ == '__main__':
    main()
