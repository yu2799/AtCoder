from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    for i in range(1, n):
        if (s[i] == "a" and s[i - 1] == "b") or (s[i] == "b" and s[i - 1] == "a"):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
