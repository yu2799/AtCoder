from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    x = 0
    res = 0
    while x + 1 < n:
        for i in range(3, 0, -1):
            if x + i < n and s[x + i] == ".":
                x += i
                break
        else:
            x += 3
            res += 1
    print(res)


if __name__ == "__main__":
    main()
