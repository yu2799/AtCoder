from sys import stdin


def main():
    input = stdin.readline
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = sum(a)
    for i in range(k + 1):
        if (i + tmp) / n >= m:
            print(i)
            return
    print(-1)


if __name__ == "__main__":
    main()
