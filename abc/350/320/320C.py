from itertools import permutations
from sys import stdin


# stop_orderの順でnumを揃えられるか？
def check(stop_order, num, s, m):
    cnt = 0
    res = 0
    for pos in stop_order:
        while cnt <= m:
            if int(s[pos][(res + cnt) % m]) == num:
                res += cnt
                cnt = 1
                break
            cnt += 1
        else:
            return -1
    return res


def main():
    input = stdin.readline
    m = int(input())
    s = [input()[:-1] for _ in range(3)]
    res = 400
    for num in range(10):
        for stop_order in permutations([0, 1, 2], 3):
            tmp = min(res, check(stop_order, num, s, m))
            if tmp != -1:
                res = min(res, tmp)
    print(res if res != 400 else -1)


if __name__ == "__main__":
    main()
