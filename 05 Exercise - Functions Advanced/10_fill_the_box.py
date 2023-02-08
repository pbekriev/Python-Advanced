def fill_the_box(*data):
    box_size = data[0] * data[1] * data[2]
    box_filled = 0

    for el in data[3:]:
        if el == "Finish":
            break
        else:
            box_filled += el

    if box_size > box_filled:
        return f"There is free space in the box. You could put {box_size - box_filled} more cubes."
    else:
        return f"No more free space! You have {box_filled - box_size} more cubes."

# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
