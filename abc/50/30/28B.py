from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    d = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for i in s:
        d[i] += 1
    print(*d.values())


if __name__ == "__main__":
    main()
