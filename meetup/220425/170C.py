from sys import stdin


def main():
    input = stdin.readline
    x, n = map(int, input().split())
    p = list(set(map(int, input().split())))
    res = 101
    diff = res - x
    for i in range(100, -1, -1):
        if i not in p:
            if abs(i - x) <= diff:
                diff = abs(i - x)
                res = i
    else:
        print(res)


if __name__ == '__main__':
    main()
