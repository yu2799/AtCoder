from sys import stdin


def main():
    input = stdin.readline
    x = input()[:-1]
    if len(set(x)) == 1:
        print("Weak")
    else:
        prev = x[0]
        for i in x[1:]:
            if (int(prev) + 1) % 10 != int(i) % 10:
                print("Strong")
                return
            prev = i
        print("Weak")


if __name__ == "__main__":
    main()
