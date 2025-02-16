numbers = [-1, 2, -3, 4, -5, 10, -23, 3, 111]

for i in range(len(numbers) - 1):
    if (numbers[i] > 0 and numbers[i + 1] > 0) or (numbers[i] < 0 and numbers[i + 1] < 0):
        print(f"{numbers[i]}, {numbers[i + 1]}")
        break

