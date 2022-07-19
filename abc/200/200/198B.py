from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    for i in range(len(n) + 1):
        s = "0" * i + n
        if s == s[::-1]:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
