from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    q = int(input())
    reset = [-1, -1]
    tmp = [[0, 0] for _ in range(n)]
    for i in range(q):
        t, *query = map(int, input().split())
        if t == 1:
            reset = [query[0], i]
        elif t == 2:
            iq = query[0] - 1
            if reset[1] > tmp[query[0] - 1][1]:
                tmp[iq][0] = 0
                a[iq] = reset[0]
            tmp[iq][0] += query[1]
            tmp[iq][1] = i
        else:
            iq = query[0] - 1
            val = a[iq] + tmp[iq][0] if reset[1] < tmp[iq][1] else reset[0]
            res.append(val)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
