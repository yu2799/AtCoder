from sys import stdin


def main():
    input = stdin.readline
    x, y, z = map(int, input().split())
    s = input()[:-1]
    res = [0, 0]
    if s[0] == "a":
        res[0] = x
        res[1] = y + z
    else:
        res[0] = y
        res[1] = x + z
    for i in s[1:]:
        _res = res[:]
        if i == "a":
            _res[0] = min(res[0] + x, res[1] + x + z)
            _res[1] = min(res[1] + y, res[0] + y + z)
        else:
            _res[0] = min(res[0] + y, res[1] + y + z)
            _res[1] = min(res[1] + x, res[0] + x + z)
        res = _res
    print(min(res))


if __name__ == "__main__":
    main()
