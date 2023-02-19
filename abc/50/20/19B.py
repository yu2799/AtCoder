from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    s_len = len(s)
    res = ""
    i = 0
    while i < s_len:
        now = s[i]
        cnt = 1
        while i + cnt < s_len and now == s[i + cnt]:
            cnt += 1
        res += f"{now}{cnt}"
        i += cnt
    print(res)


if __name__ == "__main__":
    main()
