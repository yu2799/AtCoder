from sys import stdin


def main():
    input = stdin.readline
    s = "atcoder"
    l, r = map(int, input().split())
    print(s[l - 1 : r])


if __name__ == "__main__":
    main()
