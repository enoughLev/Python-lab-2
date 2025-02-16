char_list = ['a', 'b', 'c', 'a', 'a', 3, 5, 'b', 'd', 'w']
unique_list = []

for item in char_list:
    count = 0
    for i in char_list:
        if item == i:
            count += 1
    if count == 1:
        unique_list.append(item)

print(unique_list)
