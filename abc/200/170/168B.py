from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    s = input()[:-1]
    s_len = len(s)
    if s_len <= k:
        print(s)
    else:
        print(s[:k] + "...")


if __name__ == "__main__":
    main()
