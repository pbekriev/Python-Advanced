# file = open("files/example.txt", "r")
# text = file.read()
# # file.close()
# # file.read()
# print(text)

# with open("files/example.txt", "r") as file:
#     text = file.read()
#
# print(text)

# with open("files/example.txt", "w") as file:
#     file.write("Hi...")

with open("files/example.txt", "a") as file:
    file.write("\nHello...")