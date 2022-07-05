from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    print(bin(k)[2:].replace("1", "2"))


if __name__ == "__main__":
    main()
