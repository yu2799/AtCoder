from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = []
    tmp = deque()
    for i in s:
        if not tmp:
            if i != "A":
                res.append(i)
            else:
                tmp.append(i)
        else:
            if i == "A":
                tmp.append("A")
            elif i == "B":
                if tmp[-1] == "A":
                    tmp.append("B")
                else:
                    while tmp:
                        res.append(tmp.popleft())
                    res.append("B")
            else:
                if tmp[-1] == "B":
                    tmp.pop()
                    tmp.pop()
                else:
                    while tmp:
                        res.append(tmp.popleft())
                    res.append("C")
    while tmp:
        res.append(tmp.popleft())
    print(*res, sep="")


if __name__ == "__main__":
    main()
