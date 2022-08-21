from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d = set()
    for _ in [0] * n:
        s = input()[:-1]
        if s[0] == "!":
            if s[1:] in d:
                print(s[1:])
                return
        else:
            if "!" + s in d:
                print(s)
                return
        d.add(s)
    print("satisfiable")


if __name__ == "__main__":
    main()
