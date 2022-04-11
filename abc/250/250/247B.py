from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [""] * n
    t = [""] * n
    for i in range(n):
        s[i], t[i] = input().split()
    for i in range(n):
        flag_s = False
        flag_t = False
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j]:
                flag_s = True
            if t[i] == s[j] or t[i] == t[j]:
                flag_t = True

        if flag_s and flag_t:
            print("No")
            return

    print("Yes")


if __name__ == '__main__':
    main()
