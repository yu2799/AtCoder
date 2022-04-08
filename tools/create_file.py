from sys import argv
from os import makedirs
from subprocess import Popen
from datetime import date


def input_info():
    info = []

    print("What file ? => ", end="")
    info.append(input())
    print("How many times ? => ", end="")
    info.append(int(input()))
    print("How many files to create ? => ", end="")
    info.append(int(input()))
    print(info)
    if info[-1] == 1:
        print("What problem ? => ", end="")
        info.append(input())

    return info


def main():
    cli = argv[1:]
    # コマンドライン引数が与えられなかった場合
    if not cli:
        cli = input_info()

    name = cli[0]
    times = int(cli[1])
    files = int(cli[2])
    if files == 1:
        problem = ord(cli[3].upper())
    else:
        problem = 65

    if name == "ABC":
        dir1 = (times // 50 + (times % 50 != 0)) * 50
        dir2 = (times // 10 + (times % 10 != 0)) * 10
    elif name == "meetup":
        today = date.today().strftime("%y%m%d")
        dir1 = name
        dir2 = today
    else:
        print("error!")
        return

    # フォルダを作る
    file_path = f"./{dir1}/{dir2}/"
    makedirs(file_path, exist_ok=True)

    for _ in [0] * files:
        problem = chr(problem)
        # raw文字列にしておく
        full_path = rf"{file_path}{times}{problem}.py"
        # ファイルを作って開く
        with open(full_path, "x"):
            Popen(["start", full_path], shell=True)
        problem = ord(problem) + 1


if __name__ == "__main__":
    main()
