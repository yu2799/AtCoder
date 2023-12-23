from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    d = {"t": 0, "a": 0}
    for i in s:
        if i == "T":
            d["t"] += 1
        else:
            d["a"] += 1
    if d["a"] < d["t"]:
        print("T")
    elif d["a"] > d["t"]:
        print("A")
    elif s[-1] == "A":
        print("T")
    else:
        print("A")


if __name__ == "__main__":
    main()
