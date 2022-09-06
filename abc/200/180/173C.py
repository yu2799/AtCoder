from sys import stdin


def main():
    input = stdin.readline
    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]

    b_init = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == "#":
                b_init += 1

    cnt = 0
    for bit_h in range(2**h):
        for bit_w in range(2**w):
            b_cnt = b_init
            for i in range(h):
                for j in range(w):
                    if ((bit_h >> i) & 1) or ((bit_w >> j) & 1):
                        if c[i][j] == "#":
                            b_cnt -= 1
            if b_cnt == k:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
