from sys import stdin


def main():
    input = stdin.readline
    n = list(input()[:-1])
    for i in range(len(n)):
        n[i] = "9" if n[i] == "1" else "1"
    print(*n, sep="")


if __name__ == "__main__":
    main()
