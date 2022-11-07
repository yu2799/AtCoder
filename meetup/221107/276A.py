from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = -1
    for i in range(len(s)):
        if s[i] == "a":
            res = i + 1
    print(res)


if __name__ == "__main__":
    main()
