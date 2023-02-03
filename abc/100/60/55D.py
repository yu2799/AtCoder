from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    for buf in ["SS", "SW", "WS", "WW"]:
        res = buf
        for i in range(1, n):
            if s[i] == "o":
                if res[i] == "S":
                    res += res[i - 1]
                else:
                    res += "W" if res[i - 1] == "S" else "S"
            else:
                if res[i] == "S":
                    res += "W" if res[i - 1] == "S" else "S"
                else:
                    res += res[i - 1]

        if res[-1] != res[0]:
            continue
        if res[0] == "S":
            if s[0] == "o":
                if res[-2] == res[1]:
                    print(res[:-1])
                    return
            else:
                if res[-2] != res[1]:
                    print(res[:-1])
                    return
        else:
            if s[0] == "o":
                if res[-2] != res[1]:
                    print(res[:-1])
                    return
            else:
                if res[-2] == res[1]:
                    print(res[:-1])
                    return

    print(-1)


if __name__ == "__main__":
    main()
