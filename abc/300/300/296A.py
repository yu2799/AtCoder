from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    prev = s[0]
    for i in range(1, n):
        if prev == s[i]:
            print("No")
            return
        prev = s[i]
    print("Yes")


if __name__ == "__main__":
    main()
