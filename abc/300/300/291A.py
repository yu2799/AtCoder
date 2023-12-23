from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    for i in range(len(s)):
        if "A" <= s[i] <= "Z":
            print(i + 1)
            return


if __name__ == "__main__":
    main()
