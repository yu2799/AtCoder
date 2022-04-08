s = input()
for i in range(1, len(s)+1):
    if i % 2 != 0:
        if s[i-1] == "L":
            print("No")
            exit()
    else:
        if s[i-1] == "R":
            print("No")
            exit()
print("Yes")