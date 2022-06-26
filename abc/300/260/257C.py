from sys import stdin
from bisect import bisect_right


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    w = list(map(int, input().split()))
    adult = []
    child = []
    for idx, i in enumerate(w):
        if s[idx] == "1":
            adult.append(i)
        else:
            child.append(i)
    adult.sort()
    child.sort()
    adult_len = len(adult)
    res = adult_len
    for idx, i in enumerate(child):
        adult_idx = bisect_right(adult, i)
        tmp = idx + 1 + (adult_len - adult_idx)
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
