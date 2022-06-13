from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = []
    for _ in [0] * m:
        _, *tmp = map(int, input().split())
        s.append(tmp)
    p = list(map(int, input().split()))
    res = 0
    for i in range(2**n):
        buf = list(reversed(bin(i)[2:].zfill(n)))
        for idx, j in enumerate(s):
            tmp = 0
            for k in j:
                if buf[k - 1] == "1":
                    tmp += 1
            if p[idx] != tmp % 2:
                break
        else:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
