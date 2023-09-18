from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = [0] * (n + 1)
    for x in range(1, 101):
        tmp_x = x * x
        if tmp_x > n:
            continue
        for y in range(1, 101):
            tmp_y = tmp_x + y * y + x * y
            if tmp_y > n:
                break
            for z in range(1, 101):
                tmp_z = tmp_y + z * z + y * z + z * x
                if tmp_z > n:
                    break
                res[tmp_z] += 1
    print(*res[1:], sep="\n")


if __name__ == "__main__":
    main()
