def even_odd(*data):
    command = data[-1]
    result = []
    for n in data[:-1]:
        if int(n) % 2 == 0 and command == "even":
            result.append(n)
        elif int(n) % 2 != 0 and command == "odd":
            result.append(n)

    return result

# print(even_odd(1, 2, 3, 4, 5, 6, "even"))