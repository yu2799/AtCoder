from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    for i in range(n):
        if s[i] == "|":
            for j in range(i + 1, n):
                if s[j] == "|":
                    print("out")
                    return
                if s[j] == "*":
                    print("in")
                    return


if __name__ == "__main__":
    main()
