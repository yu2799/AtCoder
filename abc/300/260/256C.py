from sys import stdin


def main():
    input = stdin.readline
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    res = 0
    for a in range(1, 29):
        for b in range(1, 29):
            tmp1 = h1 - (a + b)
            if not (1 <= tmp1 <= 28):
                continue
            for c in range(1, 29):
                tmp3 = w1 - (a + c)
                if not (1 <= tmp3 <= 28):
                    continue
                for d in range(1, 29):
                    tmp2 = h2 - (c + d)
                    if not (1 <= tmp2 <= 28):
                        continue
                    tmp4 = w2 - (b + d)
                    if not (1 <= tmp4 <= 28):
                        continue
                    tmp5 = w3 - (tmp1 + tmp2)
                    if not (1 <= tmp5 <= 28):
                        continue
                    if tmp5 == h3 - (tmp3 + tmp4):
                        res += 1
    print(res)


if __name__ == "__main__":
    main()
