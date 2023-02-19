from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = 0
    cnt = 0
    for i in s:
        if i == "A" or i == "G" or i == "C" or i == "T":
            cnt += 1
        else:
            if res < cnt:
                res = cnt
            cnt = 0
    print(max(res, cnt))


if __name__ == "__main__":
    main()
