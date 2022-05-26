from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(list)
    for i in range(n):
        s = input()[:-1]
        for idx, j in enumerate(s):
            tmp = idx
            while True:
                if tmp not in d[j]:
                    d[j].append(tmp)
                    break
                tmp += 10
    print(min([max(d[i]) for i in d.keys()]))


if __name__ == "__main__":
    main()
