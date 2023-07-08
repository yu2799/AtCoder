from sys import stdin


def main():
    input = stdin.readline
    s = [input()[:-1] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if s[i][j] == "*":
                print(f"{chr(97 + j)}{8 - i}")
                return


if __name__ == "__main__":
    main()
