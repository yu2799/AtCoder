from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    print(pi[: n + 2])


if __name__ == "__main__":
    main()
