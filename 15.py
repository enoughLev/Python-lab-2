queue = []
while True:
    command = input()

    if command.startswith("Кто последний? Я - "):
        last_name = command[len("Кто последний? Я - "):]
        queue.append(last_name)
    elif command.startswith("Я только спросить! Я - "):
        last_name = command[len("Я только спросить! Я - "):]
        queue.insert(0, last_name)
    elif command == "Следующий!":
        if queue:
            last_name = queue.pop(0)
            print(f"Заходит {last_name}!")
        else:
            print("В очереди никого нет.")
    elif command == "exit":
        break
    else:
        print("Слишком шумно. Повторите еще раз!")