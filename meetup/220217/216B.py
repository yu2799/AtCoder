from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [""] * n
    t = [""] * n
    for i in range(n):
        s[i], t[i] = input().split()
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                exit()
    else:
        print("No")


if __name__ == "__main__":
    main()
