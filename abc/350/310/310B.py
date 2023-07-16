from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    p = []
    f = []
    for _ in range(n):
        a, _, *b = map(int, input().split())
        p.append(a)
        f.append(set(b))

    for i in range(n):
        for j in range(n):
            if (
                i != j
                and p[i] >= p[j]
                and f[j] >= f[i]
                and (p[i] > p[j] or f[j] > f[i])
            ):
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
