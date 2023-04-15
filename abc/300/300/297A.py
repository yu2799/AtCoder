from sys import stdin


def main():
    input = stdin.readline
    n, d = map(int, input().split())
    t = list(map(int, input().split()))
    for i in range(n - 1):
        if t[i + 1] - t[i] <= d:
            print(t[i + 1])
            return
    print(-1)


if __name__ == "__main__":
    main()
