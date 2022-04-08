from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    i = 1
    tmp = 0
    while True:
        tmp += i
        if tmp >= n:
            print(i)
            exit()
        i += 1


if __name__ == "__main__":
    main()
