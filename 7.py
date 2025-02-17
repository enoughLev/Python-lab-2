command = input()
length = 1
space = 0
last = ""
s = command[0]
for i in range(len(command)):
    if  command[i] in "<>":
        length+=1
    if i == len(command)-1 or command[i] == "V":
        if command[i-1] == "<":
            space -= length - 1
        print(" " * space, s * length, sep="")
        if command[i-1] == ">":
            space += length - 1
        length = 1
