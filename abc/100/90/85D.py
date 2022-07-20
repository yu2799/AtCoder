from sys import stdin


def main():
    input = stdin.readline
    n, h = map(int, input().split())
    a = []
    b = []
    for _ in [0] * n:
        i, j = map(int, input().split())
        a.append(i)
        b.append(j)
    a.sort()
    b.sort(reverse=True)
    res = 0
    tmp = a[-1]
    for i in b:
        if i >= tmp:
            res = res + 1
            h = h - i
            if h <= 0:
                print(res)
                return
        else:
            break

    res = res + ((h + tmp - 1) // tmp)
    print(res)


if __name__ == "__main__":
    main()
