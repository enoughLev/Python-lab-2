numbers = input()
length = len(numbers)
i = 0
current_num = 0
next_num = 0

while i < length-1:
    current_num = numbers[i]
    next_num = numbers[i+1]
    if current_num < next_num: print(next_num)
    i += 1

