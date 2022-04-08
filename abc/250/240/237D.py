from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    res = [n] * (n + 1)
    r = 0
    l = n
    for i in range(len(s)):
        if s[i] == "R":
            res[r] = i
            r += 1
        else:
            res[l] = i
            l -= 1
    print(*res, sep=" ")


if __name__ == "__main__":
    main()
