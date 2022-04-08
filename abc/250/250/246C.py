from sys import stdin


def main():
    input = stdin.readline
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    res = sum(a)
    tmp = k
    q = sum([i // x for i in a])
    r = sorted((i % x for i in a), reverse=True)
    res -= x * min(k, q)
    tmp -= min(k, q)
    res -= sum(r[:tmp])
    print(res)


if __name__ == "__main__":
    main()
