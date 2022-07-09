from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    s = deque(list(input()[:-1]))
    t = deque(list(input()[:-1]))
    if len(s) > len(t):
        print("No")
        return

    prev = ""
    while s or t:
        if s:
            if s[0] == t[0]:
                rm = s.popleft()
                t.popleft()
                if rm != prev:
                    cnt = 1
                    prev = rm
                else:
                    cnt += 1
            else:
                if prev == t[0] and cnt >= 2:
                    while prev == t[0]:
                        t.popleft()
                else:
                    print("No")
                    return
        else:
            if prev == t[0] and cnt >= 2:
                while t:
                    rm = t.popleft()
                    if rm != prev:
                        print("No")
                        return
            else:
                print("No")
                return

    if s or t:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
