from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = []
    for i in s:
        if i == "B":
            if res:
                res.pop()
        else:
            res.append(i)
    print(*res, sep="")


if __name__ == "__main__":
    main()
