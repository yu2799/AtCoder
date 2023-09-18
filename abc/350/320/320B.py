from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    l = len(s)
    res = 0
    for i in range(l):
        for j in range(i, l):
            tmp = s[i : j + 1]
            if tmp == tmp[::-1]:
                res = max(res, j - i + 1)
    print(res)


if __name__ == "__main__":
    main()
