from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    s_cnt = [0] * 26
    t_cnt = [0] * 26
    for i in range(ord("a"), ord("z") + 1):
        s_cnt[i - 97] = s.count(chr(i))
        t_cnt[i - 97] = t.count(chr(i))
    s_cnt.sort()
    t_cnt.sort()
    print("Yes" if s_cnt == t_cnt else "No")


if __name__ == "__main__":
    main()
