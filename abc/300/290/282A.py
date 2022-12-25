from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    buf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(buf[:k])


if __name__ == "__main__":
    main()
