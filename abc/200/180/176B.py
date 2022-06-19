from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    print(
        "Yes"
        if sum([n.count(str(i)) * i for i in range(1, 10)]) % 9 == 0
        else "No"
    )


if __name__ == "__main__":
    main()
