from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    res = [set() for _ in [0] * n]
    for _ in [0] * m:
        k, *x = map(int, input().split())
        for i in range(k - 1):
            for j in range(i + 1, k):
                res[x[i] - 1].add(x[j])
                res[x[j] - 1].add(x[i])
    for i in res:
        if len(i) != n - 1:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
