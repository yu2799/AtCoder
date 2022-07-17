from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    f = [list(input().split()) for _ in [0] * n]
    p = [list(map(int, input().split())) for _ in [0] * n]
    res = -(10**9)
    for i in range(1, pow(2, 10)):
        tmp = 0
        for idx, j in enumerate(f):
            cnt = 0
            for a, b in zip(bin(i)[2:].zfill(10), j):
                if a == "1" and a == b:
                    cnt = cnt + 1
            tmp = tmp + p[idx][cnt]
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
