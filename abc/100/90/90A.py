from sys import stdin


def main():
    input = stdin.readline
    c = [input()[:-1] for _ in [0] * 3]
    print(c[0][0] + c[1][1] + c[2][2])


if __name__ == "__main__":
    main()
