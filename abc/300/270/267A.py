from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    if s == "Monday":
        print(5)
    elif s == "Tuesday":
        print(4)
    elif s == "Wednesday":
        print(3)
    elif s == "Thursday":
        print(2)
    else:
        print(1)


if __name__ == "__main__":
    main()
