from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    buf = ""
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        buf += i * n
    print(buf[x - 1])


if __name__ == "__main__":
    main()
