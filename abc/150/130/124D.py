from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    s = input()[:-1]
    cnt = 0
    res = 0
    q = deque()
    prev = "1"
    for r in s:
        q.append(r)
        if prev == "1" and r == "0":
            cnt += 1
            if k < cnt:
                if res < len(q) - 1:
                    res = len(q) - 1
            while q and k < cnt:
                rm = q.popleft()
                if rm == "0" and q[0] == "1":
                    cnt -= 1
        prev = r
    print(res if len(q) < res else len(q))


if __name__ == "__main__":
    main()
