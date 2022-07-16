from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    s_len = len(s)
    t_len = len(t)
    idx = -1
    for i in range(s_len):
        if s[i] == t[0] or s[i] == "?":
            for j in range(1, t_len):
                if i + j >= s_len or s[i + j] != t[j] and s[i + j] != "?":
                    break
            else:
                idx = i
    if idx == -1:
        print("UNRESTORABLE")
    else:
        res = ""
        cnt = 0
        while cnt < s_len:
            if cnt != idx:
                if s[cnt] == "?":
                    res = res + "a"
                else:
                    res = res + s[cnt]
                cnt = cnt + 1
            else:
                res = res + t
                cnt = cnt + t_len
        print(res)


if __name__ == "__main__":
    main()
