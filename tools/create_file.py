from sys import argv
from os import makedirs
from subprocess import Popen
from datetime import date
from time import sleep


def input_info():
    info = []

    print("What file ? => ", end="")
    info.append(input())
    print("How many times ? => ", end="")
    info.append(int(input()))
    print("How many files to create ? => ", end="")
    info.append(int(input()))
    if info[-1] == 1:
        print("What problem ? => ", end="")
        info.append(input())

    return info


def main():
    cli = argv[1:]
    # コマンドライン引数が与えられなかった場合
    if not cli:
        cli = input_info()

    name = cli[0].lower()
    times = int(cli[1])
    files = int(cli[2])
    if files == 1:
        problem = ord(cli[3].upper())
    else:
        problem = 65

    if name == "abc" or name == "arc":
        dir1 = f"/{(times + 50 - 1) // 50 * 50}"
        dir2 = f"/{(times + 10 - 1) // 10 * 10}"
    elif name == "meetup":
        today = date.today().strftime("%y%m%d")
        dir1 = "/" + today
        dir2 = ""
    else:
        print("error!")
        return

    # フォルダを作る
    file_path = f"./{name}{dir1}{dir2}"
    makedirs(file_path, exist_ok=True)

    for _ in [0] * files:
        problem = chr(problem)
        # raw文字列にしておく
        full_path = rf"{file_path}/{times}{problem}.py"
        # ファイルを作って開く
        with open(full_path, "x"):
            Popen(["start", full_path], shell=True)
        sleep(1 // 2)
        problem = ord(problem) + 1


if __name__ == "__main__":
    main()
