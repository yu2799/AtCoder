from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = 10**10
    for i in range(len(s) - 2):
        tmp = abs(int(s[i]) * 100 + int(s[i + 1]) * 10 + int(s[i + 2]) - 753)
        if tmp < res:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
