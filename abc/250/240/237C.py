from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    i = 0
    if len(set(s)) == 1:
        print("Yes")
        exit()
    l = 0
    r = len(s) - 1
    while s[r] == "a":
        r -= 1
        if s[l] == "a":
            l += 1
    while l <= r:
        if s[l] != s[r]:
            print("No")
            exit()
        l += 1
        r -= 1
    print("Yes")


if __name__ == "__main__":
    main()
