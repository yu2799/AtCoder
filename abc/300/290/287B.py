from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = [input()[:-1] for _ in range(n)]
    t = set([input()[:-1] for _ in range(m)])
    res = 0
    for i in s:
        if i[-3:] in t:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
