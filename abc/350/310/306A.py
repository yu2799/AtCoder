from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    res = ""
    for i in s:
        res += i + i
    print(res)


if __name__ == "__main__":
    main()
