import os

while True:
    command, *info = input().split('-')

    if command == 'End':
        break

    elif command == 'Create':
        file = open(f'{info[0]}', 'w')
        file.close()

    elif command == 'Add':
        with open(f'{info[0]}', 'a') as file:
            file.write(f'{info[1]}\n')
    elif command == 'Replace':
        try:
            with open(f'{info[0]}', 'r') as f:
                text = f.read()

            text = text.replace(info[1], info[2])

            with open(f'{info[0]}', 'w') as f:
                f.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif command == 'Delete':
        try:
            os.remove(f'{info[0]}')
        except FileNotFoundError:
            print("An error occurred")
