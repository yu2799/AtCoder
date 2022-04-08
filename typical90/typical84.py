from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    res = 0
    l = 0
    mark = s[0]
    sLen = len(s)
    for r in range(sLen):
        if s[r] != mark:
            res += (sLen - r) * (r - l)
            l = r
            mark = s[r]
    print(res)


if __name__ == '__main__':
    main()
