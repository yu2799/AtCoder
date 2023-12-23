from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = input()[:-1].split("0")
    res = 0
    for i in s:
        a = 0
        b = 0
        for j in i:
            if j == "1":
                a += 1
            else:
                b += 1
        if a != 0:
            a = max(a - m, 0)
        res = max(res, a + b)
    print(res)


if __name__ == "__main__":
    main()
