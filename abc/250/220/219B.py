from sys import stdin


def main():
    input = stdin.readline
    s = [input()[:-1] for _ in [0] * 3]
    t = input()[:-1]
    res = ""
    for i in t:
        res += s[int(i) - 1]
    print(res)


if __name__ == "__main__":
    main()
