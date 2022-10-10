from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    res = ["2" if i == "1" else "0" for i in bin(k)[2:]]
    print(*res, sep="")


if __name__ == "__main__":
    main()
