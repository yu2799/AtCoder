from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xy = []
    for _ in [0] * n:
        a = int(input())
        tmp = [tuple(map(int, input().split())) for _ in [0] * a]
        xy.append(tmp)

    res = 0
    for i in range(1, 2**n):
        buf = bin(i)[2:].zfill(n)
        honest = [False] * n
        for idx, j in enumerate(buf):
            if j == "1":
                honest[idx] = True
        for idx, j in enumerate(buf):
            if j == "1":
                for x, y in xy[idx]:
                    if honest[x - 1] != y:
                        break
                else:
                    continue
                break
        else:
            tmp = buf.count("1")
            if res < tmp:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
