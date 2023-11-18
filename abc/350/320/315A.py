from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = []
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            continue
        res.append(i)
    print("".join(res))


if __name__ == "__main__":
    main()
