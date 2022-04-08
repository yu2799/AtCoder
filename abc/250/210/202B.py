S = input()
res = []
for i in reversed(S):
    if i == "6":
        print("9", end="")
    elif i == "9":
        print("6", end="")
    else:
        print(i, end="")
