from sys import stdin


def main():
    input = stdin.readline
    o = input()[:-1]
    e = input()[:-1]
    for i, j in zip(o, e):
        print(i, j, sep="", end="")
    if len(o) - len(e) == 1:
        print(o[-1])


if __name__ == "__main__":
    main()
