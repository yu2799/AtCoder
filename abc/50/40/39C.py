from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    if "WBWBWWBWBWBW" not in s:
        print("Re")
        return

    idx = s.index("WBWBWWBWBWBW")

    if idx == 0:
        print("Do")
    elif idx == 1:
        print("Si")
    elif idx == 3:
        print("La")
    elif idx == 5:
        print("So")
    elif idx == 7:
        print("Fa")
    else:
        print("Mi")


if __name__ == "__main__":
    main()
