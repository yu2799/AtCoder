from sys import stdin


def main():
    input = stdin.readline
    k, g, m = map(int, input().split())
    res = [0, 0]
    for _ in range(k):
        if res[0] == g:
            res[0] = 0
        elif res[1] == 0:
            res[1] = m
        else:
            if g < res[1]:
                res[0], res[1] = g, res[1] - (g - res[0])
            else:
                res[0], res[1] = res[1], 0

    print(*res)


if __name__ == "__main__":
    main()
