from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    sum_n = sum([int(i) for i in n])
    print("Yes" if int(n) % sum_n == 0 else "No")


if __name__ == "__main__":
    main()
