from sys import stdin


def main():
    input = stdin.readline
    s = [""] * 3
    res = ["ABC", "ARC", "AGC", "AHC"]
    for i in range(3):
        s[i] = input()[:-1]
    for i in res:
        if i not in s:
            print(i)
            break


if __name__ == "__main__":
    main()
