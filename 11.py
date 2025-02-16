my_list = [1, 2, 3, 4, 5, 6, 7, 8]
list_length = len(my_list)

for i in range(0, list_length - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
