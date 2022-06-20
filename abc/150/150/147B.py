from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    n = (len(s) + 1) // 2
    sl = s[:n]
    sr = s[n:]
    sr = sr[::-1]
    res = 0
    for i, j in zip(sl, sr):
        if i != j:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
