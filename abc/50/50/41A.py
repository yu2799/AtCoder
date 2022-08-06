from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    i = int(input())
    print(s[i - 1])


if __name__ == "__main__":
    main()
