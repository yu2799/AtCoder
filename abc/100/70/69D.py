from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    tmp = []
    l = 0
    for idx, i in enumerate(a):
        if i + l < w:
            l += i
            for _ in [0] * i:
                tmp.append(idx + 1)
        else:
            while i > 0:
                if i + l < w:
                    l += i
                    for _ in [0] * i:
                        tmp.append(idx + 1)
                    break
                else:
                    for _ in [0] * (w - l):
                        tmp.append(idx + 1)
                    res.append(tmp)
                    tmp = []
                    i -= (w - l)
                    l = 0
    for i, j in enumerate(res):
        if i % 2:
            print(*list(reversed(j)), sep=" ")
        else:
            print(*j, sep=" ")


if __name__ == '__main__':
    main()
