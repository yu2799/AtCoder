from sys import stdin


def main():
    input = stdin.readline
    p, q = input().split()
    tmp = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}
    print(abs(tmp[q] - tmp[p]))


if __name__ == "__main__":
    main()
