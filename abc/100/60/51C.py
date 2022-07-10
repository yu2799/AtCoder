from sys import stdin


def main():
    input = stdin.readline
    sx, sy, tx, ty = map(int, input().split())
    res = ""
    res += (ty - sy) * "U" + (tx - sx) * "R"
    res += (ty - sy) * "D" + (tx - sx) * "L"
    res += "L" + (ty - sy + 1) * "U" + (tx - sx + 1) * "R" + "D"
    res += "R" + (ty - sy + 1) * "D" + (tx - sx + 1) * "L" + "U"
    print(res)


if __name__ == "__main__":
    main()
