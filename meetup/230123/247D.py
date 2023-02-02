from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    q = int(input())
    res = []
    d = deque()
    for _ in [0] * q:
        query = list(map(int, input().split()))
        if query[0] == 1:
            d.append([query[1], query[2]])
        else:
            tmp = 0
            num = query[1]
            while d and num > 0:
                rm = d.popleft()
                if rm[1] <= num:
                    tmp += rm[0] * rm[1]
                    num -= rm[1]
                else:
                    tmp += rm[0] * num
                    rm[1] -= num
                    num = 0
                    d.appendleft(rm)
            res.append(tmp)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
