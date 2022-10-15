from bisect import bisect_left
from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    r_list = defaultdict(list)
    c_list = defaultdict(list)
    for _ in [0] * n:
        r, c = map(int, input().split())
        r_list[r].append(c)
        c_list[c].append(r)
    for key in r_list.keys():
        r_list[key].sort()
    for key in c_list.keys():
        c_list[key].sort()
    res = []
    q = int(input())
    for _ in [0] * q:
        d, move = input().split()
        move = int(move)
        if d == "L":
            if r_list[rs]:
                idx = bisect_left(r_list[rs], cs)
                if idx != 0:
                    cs = max(r_list[rs][idx - 1] + 1, cs - move, 1)
                else:
                    cs = max(cs - move, 1)
            else:
                cs = max(cs - move, 1)
        elif d == "R":
            if r_list[rs]:
                idx = bisect_left(r_list[rs], cs)
                if len(r_list[rs]) != idx:
                    cs = min(r_list[rs][idx] - 1, cs + move, w)
                else:
                    cs = min(cs + move, w)
            else:
                cs = min(cs + move, w)
        elif d == "U":
            if c_list[cs]:
                idx = bisect_left(c_list[cs], rs)
                if idx != 0:
                    rs = max(c_list[cs][idx - 1] + 1, rs - move, 1)
                else:
                    rs = max(rs - move, 1)
            else:
                rs = max(rs - move, 1)
        else:
            if c_list[cs]:
                idx = bisect_left(c_list[cs], rs)
                if len(c_list[cs]) != idx:
                    rs = min(c_list[cs][idx] - 1, rs + move, h)
                else:
                    rs = min(rs + move, h)
            else:
                rs = min(rs + move, h)
        res.append((rs, cs))

    for i in range(q):
        print(*res[i])


if __name__ == "__main__":
    main()
