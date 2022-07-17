from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    res = 0
    for i, j in zip(s, t):
        if i != j:
            res = res + 1
    print(res)


if __name__ == "__main__":
    main()
