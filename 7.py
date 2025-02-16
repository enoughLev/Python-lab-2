"""snail_path = input()
trace = snail_path[0]
snail_path = snail_path[1::]
spaces = 0
i = 0

while True:
    if snail_path[i] == ">":
        print(" "*spaces, end='')
        print(trace, end='')
        spaces+=1
    elif snail_path[i] == "<":
        print(" "*spaces + trace, end='')
        spaces-=1
    elif snail_path[i] == "V":
        print(" "*spaces + trace)

    i+=1"""

snail_path = ".VVV>>>VVVV<<"
trace = snail_path[0]
snail_path = snail_path[1::]
way = list()
spaces = 0
count = 0

for path in snail_path:
    if path == "V":
        count += 1
        way.append(" " * spaces)
        way.append(trace * count)
