from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    b_pos1, b_pos2, r_pos1, r_pos2 = -1, -1, -1, -1
    for i in range(len(s)):
        if s[i] == "B":
            if b_pos1 == -1:
                b_pos1 = i
            else:
                b_pos2 = i
        if s[i] == "R":
            if r_pos1 == -1:
                r_pos1 = i
            else:
                r_pos2 = i
    if b_pos1 % 2 != b_pos2 % 2 and r_pos1 < s.find("K") < r_pos2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
