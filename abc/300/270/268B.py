from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    if len(s) > len(t):
        print("No")
        return
    for i, j in zip(s, t):
        if i != j:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
