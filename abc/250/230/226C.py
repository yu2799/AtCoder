from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [[] for _ in [0] * n]
    t = [0] * n
    for i in range(n):
        t[i], _, *a[i] = map(int, input().split())

    res = 0
    req = [False] * n
    req[n - 1] = True
    for i in range(n - 1, -1, -1):
        if req[i]:
            res += t[i]
            for j in a[i]:
                req[j - 1] = True
    print(res)


if __name__ == "__main__":
    main()
