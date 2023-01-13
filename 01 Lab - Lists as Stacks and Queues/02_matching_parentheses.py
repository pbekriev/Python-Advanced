data = input()
indexes = []

for i in range(len(data)):
    char = data[i]

    if char == "(":
        indexes.append(i)
    elif char == ")":
        last_i = indexes.pop()
        print(data[last_i:i+1])
        