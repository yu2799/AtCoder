from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    res = []
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                res.append("(")
                cnt = 0
    res.append(s + ")" * cnt)
    print(*res, sep="")


if __name__ == '__main__':
    main()
