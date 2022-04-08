from sys import stdin


def main():
    input = stdin.readline
    l = 10 ** 5
    r = l + 1
    a = [0] * (l * 2 + 1)

    q = int(input())
    res = []
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            a[l] = x
            l -= 1
        elif t == 2:
            a[r] = x
            r += 1
        else:
            res.append(a[l + x])
    print(*res, sep="\n")

    # input = stdin.readline
    # q = int(input())
    # u = []
    # l = []
    # for _ in range(q):
    #     t, x = map(int, input().split())
    #     if t == 1:
    #         u.append(x)
    #     elif t == 2:
    #         l.append(x)
    #     else:
    #         if x <= len(u):
    #             print(u[-x])
    #         else:
    #             print(l[x - len(u) - 1])


if __name__ == '__main__':
    main()
