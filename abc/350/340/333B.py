from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    d = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
    }
    a = abs(d[s[0]] - d[s[1]])
    b = abs(d[t[0]] - d[t[1]])
    if a == 3:
        a = 2
    elif a == 4:
        a = 1
    if b == 3:
        b = 2
    elif b == 4:
        b = 1
    print("Yes" if a == b else "No")


if __name__ == "__main__":
    main()
