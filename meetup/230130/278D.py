from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    q = int(input())
    base = 0
    change = -1
    prev = [-1] * n
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            base = query[1]
            change = i
        elif query[0] == 2:
            iq = query[1] - 1
            xq = query[2]
            if prev[iq] < change:
                a[iq] = base + xq
            else:
                a[iq] += xq
            prev[iq] = i
        else:
            iq = query[1] - 1
            res.append(a[iq] if prev[iq] >= change else base)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
