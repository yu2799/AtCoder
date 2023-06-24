from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    tmp = [""] * (n + 1)
    cnt = 0
    for i in range(n):
        if s[i] == "(":
            cnt += 1
            tmp[cnt] += s[i]
        elif s[i] == ")" and tmp[cnt] and tmp[cnt][0] == "(":
            tmp[cnt] = ""
            cnt -= 1
        else:
            tmp[cnt] += s[i]
    res = ""
    for i in tmp:
        res += i
    print(res)


if __name__ == "__main__":
    main()
