from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    for i in range(256):
        if bin(a ^ i) == bin(b):
            print(i)
            return


if __name__ == "__main__":
    main()
