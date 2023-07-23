from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(5 - day.index(s))


if __name__ == "__main__":
    main()
