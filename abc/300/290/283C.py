from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = len(s)
    prev = ""
    for i in s:
        if i == "0" and prev == "0":
            res -= 1
            prev = ""
        else:
            prev = i
    print(res)


if __name__ == "__main__":
    main()
