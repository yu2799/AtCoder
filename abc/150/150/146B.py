from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    res = ""
    buf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        res += buf[(buf.index(i) + n) % 26]
    print(res)


if __name__ == "__main__":
    main()
