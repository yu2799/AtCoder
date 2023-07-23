from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    d = {"A": 0, "B": 0, "C": 0}
    for i in range(n):
        d[s[i]] += 1
        if d["A"] > 0 and d["B"] > 0 and d["C"] > 0:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
