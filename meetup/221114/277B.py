from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d = {}
    type = {"H", "D", "S", "C"}
    num = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
    for _ in [0] * n:
        s = input()[:-1]
        if s[0] in type and s[1] in num and s not in d:
            d[s] = True
        else:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
