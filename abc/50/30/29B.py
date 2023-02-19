from sys import stdin


def main():
    input = stdin.readline
    res = 0
    for _ in range(12):
        s = input()[:-1]
        if "r" in s:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
