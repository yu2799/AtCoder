from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    c = input()[:-1]
    r_cnt = c.count("R")
    pos = 0
    res = 0
    while pos < n:
        if r_cnt > 0:
            if c[pos] == "W":
                res += 1
            r_cnt -= 1
        else:
            break
        pos += 1
    print(res)


if __name__ == "__main__":
    main()
