from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    t = input()[:-1]
    tmp = pow(10, 10)
    if t == "1":
        print(tmp * 2)
    elif t == "11":
        print(tmp)
    elif "00" in t or "010" in t or "111" in t:
        print(0)
    else:
        cnt = t.count("0")
        print(tmp - cnt + (1 if t[-1] == "0" else 0))


if __name__ == "__main__":
    main()
