from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = []
    for _ in [0] * (len(s)):
        s = s[1:] + s[0]
        res.append(s)
    res.sort()
    print(res[0])
    print(res[-1])


if __name__ == "__main__":
    main()
