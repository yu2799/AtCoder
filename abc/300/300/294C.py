from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(sorted(a + b))
    cnt = 0
    res = [[] for _ in range(2)]
    for i in range(n + m):
        if cnt < n and c[i] == a[cnt]:
            res[0].append(i + 1)
            cnt += 1
        else:
            res[1].append(i + 1)
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
