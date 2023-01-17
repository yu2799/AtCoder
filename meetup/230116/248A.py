from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    for i in range(10):
        if s.count(str(i)) == 0:
            print(i)


if __name__ == "__main__":
    main()
