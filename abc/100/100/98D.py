from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    tmp = 0
    tmp_sum = 0
    tmp_bin = 0
    q = deque()
    for r in a:
        q.append(r)
        tmp_sum += r
        tmp_bin ^= r
        tmp += 1
        while q and tmp_sum != tmp_bin:
            rm = q.popleft()
            tmp_sum -= rm
            tmp_bin ^= rm
            tmp -= 1
        res += tmp
    print(res)


if __name__ == "__main__":
    main()
