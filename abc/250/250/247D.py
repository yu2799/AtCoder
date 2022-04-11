from sys import stdin


def main():
    input = stdin.readline
    q = int(input())
    res = []
    cnt = 0
    d = []
    for _ in [0] * q:
        *query, = map(int, input().split())
        if query[0] == 1:
            d.append([query[1], query[2]])
        else:
            if query[1] <= d[cnt][1]:
                res.append(query[1] * d[cnt][0])
                d[cnt][1] -= query[1]
            else:
                tmp = 0
                while query[1] > 0:
                    if query[1] <= d[cnt][1]:
                        tmp += query[1] * d[cnt][0]
                        d[cnt][1] -= query[1]
                        break
                    else:
                        tmp += d[cnt][0] * d[cnt][1]
                        query[1] -= d[cnt][1]
                        cnt += 1
                res.append(tmp)
    print(*res, sep="\n")


if __name__ == '__main__':
    main()
