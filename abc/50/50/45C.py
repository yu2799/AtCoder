from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = 0
    len_s = len(s) - 1
    for i in range(2**len_s):
        buf = bin(i)[2:].zfill(len_s)
        prev = 0
        for idx, j in enumerate(buf):
            if j == "1":
                res += int(s[prev : idx + 1])
                prev = idx + 1
        res += int(s[prev:])
    print(res)


if __name__ == "__main__":
    main()
