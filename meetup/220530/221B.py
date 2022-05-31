from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    for i in range(len(s) - 1):
        if s[i] != t[i]:
            if s[i] == t[i + 1] and s[i + 1] == t[i]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("Yes")


if __name__ == "__main__":
    main()
