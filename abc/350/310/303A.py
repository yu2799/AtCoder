from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    t = input()[:-1]
    for i, j in zip(s, t):
        if not (
            i == j
            or (i == "1" and j == "l")
            or (i == "l" and j == "1")
            or (i == "0" and j == "o")
            or (i == "o" and j == "0")
        ):
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
