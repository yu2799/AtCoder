from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    tmp = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - tmp.index(s))


if __name__ == "__main__":
    main()
