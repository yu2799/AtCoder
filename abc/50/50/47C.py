from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    prev = s[0]
    res = 0
    for i in s[1:]:
        if prev != i:
            res += 1
            prev = i
    print(res)


if __name__ == "__main__":
    main()
