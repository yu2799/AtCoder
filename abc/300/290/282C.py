from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    res = []
    cnt = 0
    for i in s:
        if i == '"':
            cnt += 1
        if i == "," and cnt % 2 == 0:
            i = "."
        res.append(i)
    print(*res, sep="")


if __name__ == "__main__":
    main()
