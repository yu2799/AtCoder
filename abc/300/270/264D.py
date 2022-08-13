from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    res = 0
    d = {"a": 0, "t": 1, "c": 2, "o": 3, "d": 4, "e": 5, "r": 6}
    for i in range(7):
        for j in range(7 - i - 1):
            if d[s[j]] > d[s[j + 1]]:
                s[j], s[j + 1] = s[j + 1], s[j]
                res += 1
    print(res)


if __name__ == "__main__":
    main()
