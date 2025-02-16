bow = input()
length = len(bow)
height = (length // 2) + 1

if length % 2 == 0:
    center_start = length // 2 - 1
    center_end = length // 2 + 1
    print(' ' * (height - 1) + bow[center_start:center_end])
    index = center_end
    left_index = center_start - 1
    width = 2
else:
    center = length // 2
    print(' ' * (height - 1) + bow[center])
    index = center + 1
    left_index = center - 1
    width = 1

for i in range(1, height):
    spaces = ' ' * (height - i - 1)
    if left_index >= 0 and index < length:
        level = spaces + bow[left_index] + ' ' * width + bow[index]
        print(level)
        left_index -= 1
        index += 1
        width += 2
