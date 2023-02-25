def get_player_position(matrix, player):
    for row_index, row_data in enumerate(matrix):
        if player in row_data:
            return row_index, row_data.index(player)


def create_playground(data):
    row, columns = data
    matrix = []
    for _ in range(row):
        matrix.append(input().split())
    return matrix


data = list(map(int, input().split()))
playground = create_playground(data)

moves_made = 0
touched_opponents = 0

player_position = get_player_position(playground, "B")
current_player_row, current_player_column = player_position

while True:
    command = input()

    if command == "Finish":
        break

    if command == "up" and current_player_row >= 1:
        if playground[current_player_row - 1][current_player_column] == "-":
            current_player_row -= 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row + 1][current_player_column] = "-"
            moves_made += 1
        elif playground[current_player_row - 1][current_player_column] == "P":
            current_player_row -= 1
            touched_opponents += 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row + 1][current_player_column] = "-"
            moves_made += 1

    elif command == "down" and current_player_row < data[0] - 1:
        if playground[current_player_row + 1][current_player_column] == "-":
            current_player_row += 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row - 1][current_player_column] = "-"
            moves_made += 1
        elif playground[current_player_row + 1][current_player_column] == "P":
            current_player_row += 1
            touched_opponents += 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row - 1][current_player_column] = "-"
            moves_made += 1

    elif command == "right" and current_player_column < data[1] - 1:
        if playground[current_player_row][current_player_column + 1] == "-":
            current_player_column += 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row][current_player_column - 1] = "-"
            moves_made += 1
        elif playground[current_player_row][current_player_column + 1] == "P":
            current_player_column += 1
            touched_opponents += 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row][current_player_column - 1] = "-"
            moves_made += 1

    elif command == "left" and current_player_column > 0:
        if playground[current_player_row][current_player_column - 1] == "-":
            current_player_column -= 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row][current_player_column + 1] = "-"
            moves_made += 1
        elif playground[current_player_row][current_player_column - 1] == "P":
            current_player_column -= 1
            touched_opponents += 1
            playground[current_player_row][current_player_column] = "B"
            playground[current_player_row][current_player_column + 1] = "-"
            moves_made += 1

    if touched_opponents == 3:
        break

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves_made}")
