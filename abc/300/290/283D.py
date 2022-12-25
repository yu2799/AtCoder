from collections import defaultdict, deque
from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    num = deque()
    q = deque()
    d = defaultdict(int)
    for idx, i in enumerate(s):
        if i == "(":
            num.append(idx)
        elif i == ")":
            rm = num.pop()
            while q and q[-1][1] > rm:
                tmp = q.pop()
                d[tmp[0]] -= 1
        else:
            if d[i]:
                print("No")
                return
            d[i] += 1
            q.append((i, idx))
    print("Yes")


if __name__ == "__main__":
    main()
