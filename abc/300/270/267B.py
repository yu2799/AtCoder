from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    if s[0] == "1":
        print("No")
    else:
        if s[3] == "1" and s[4] == "1" and s[1] == "0" and s[7] == "0":
            print("Yes")
        elif s[4] == "1" and s[5] == "1" and s[2] == "0" and s[8] == "0":
            print("Yes")
        elif (
            s[3] == "1"
            and s[5] == "1"
            and s[1] == "0"
            and s[2] == "0"
            and s[7] == "0"
            and s[8] == "0"
        ):
            print("Yes")
        elif s[6] == "1" and (s[1] == "1" or s[7] == "1") and s[3] == "0":
            print("Yes")
        elif s[9] == "1" and s[5] == "0" and (s[2] == "1" or s[8] == "1"):
            print("Yes")
        elif (
            s[9] == "1"
            and s[4] == "1"
            and s[2] == "0"
            and s[5] == "0"
            and s[8] == "0"
        ):
            print("Yes")
        elif (
            s[9] == "1"
            and (s[1] == "1" or s[7] == "1")
            and s[2] == "0"
            and s[4] == "0"
            and s[5] == "0"
            and s[8] == "0"
        ):
            print("Yes")
        elif (
            s[9] == "1"
            and s[3] == "1"
            and s[1] == "0"
            and s[2] == "0"
            and s[4] == "0"
            and s[5] == "0"
            and s[7] == "0"
            and s[8] == "0"
        ):
            print("Yes")

        elif (
            s[6] == "1"
            and s[9] == "1"
            and s[1] == "0"
            and s[2] == "0"
            and s[3] == "0"
            and s[4] == "0"
            and s[5] == "0"
            and s[7] == "0"
            and s[8] == "0"
        ):
            print("Yes")
        elif (
            s[6] == "1"
            and s[5] == "1"
            and s[1] == "0"
            and s[2] == "0"
            and s[3] == "0"
            and s[4] == "0"
            and s[7] == "0"
            and s[8] == "0"
        ):
            print("Yes")
        elif (
            s[6] == "1"
            and (s[2] == "1" or s[8] == "1")
            and s[1] == "0"
            and s[3] == "0"
            and s[4] == "0"
            and s[7] == "0"
        ):
            print("Yes")
        elif (
            s[6] == "1"
            and s[4] == "1"
            and s[1] == "0"
            and s[3] == "0"
            and s[7] == "0"
        ):
            print("Yes")
        elif s[6] == "1" and (s[1] == "1" or s[7] == "1") and s[3] == "0":
            print("Yes")

        elif s[5] == "0" and s[9] == "1" and (s[2] == "1" or s[8] == "1"):
            print("Yes")
        elif (
            s[4] == "0"
            and (s[1] == "1" or s[7] == "1")
            and (s[2] == "1" or s[8] == "1")
        ):
            print("Yes")
        elif (
            s[3] == "1"
            and (s[2] == "1" or s[8] == "1")
            and s[1] == "0"
            and s[4] == "0"
            and s[7] == "0"
        ):
            print("Yes")
        elif (
            s[5] == "1"
            and (s[1] == "1" or s[7] == "1")
            and s[2] == "0"
            and s[4] == "0"
            and s[8] == "0"
        ):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
