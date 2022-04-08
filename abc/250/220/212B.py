from sys import stdin


def main():
    input = stdin.readline
    x = input()[:-1]
    prev = int(x[0])
    if len(set(x)) == 1:
        print("Weak")
        return
    for i in x[1:]:
        if (prev + 1) % 10 != int(i):
            print("Strong")
            return
        prev = int(i)
    print("Weak")


if __name__ == "__main__":
    main()
