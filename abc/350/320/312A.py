from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    a = {"ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"}
    print("Yes" if s in a else "No")


if __name__ == "__main__":
    main()
