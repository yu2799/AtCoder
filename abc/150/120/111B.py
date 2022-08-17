from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    for i in range(1, 10):
        if i * 111 >= n:
            print(i * 111)
            return


if __name__ == "__main__":
    main()
