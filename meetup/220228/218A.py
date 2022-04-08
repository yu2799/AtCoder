from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    print("Yes" if s[n-1] == "o" else "No")


if __name__ == '__main__':
    main()