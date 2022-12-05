from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    d = {"w": 0, "v": 0}
    for i in s:
        d[i] += 1
    print(d["w"] * 2 + d["v"])


if __name__ == "__main__":
    main()
