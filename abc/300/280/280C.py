from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i + 1)
            return
    print(len(t))


if __name__ == "__main__":
    main()
