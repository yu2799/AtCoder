from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    f_cnt = 1
    t_cnt = 1
    for _ in [0] * n:
        s = input()[:-1]
        if s == "AND":
            f_cnt = f_cnt * 2 + t_cnt
        else:
            t_cnt = t_cnt * 2 + f_cnt
    print(t_cnt)


if __name__ == "__main__":
    main()
