from string import punctuation
with open("text1.txt") as my_file:
    my_list=my_file.readlines()
my_output=open("output.txt","w")
for my_list_row in range(len(my_list)):
    letters,marks=0,0
    for letter in my_list[my_list_row]:
        if ord("a")<=ord(letter)<=ord("z") or ord("A")<=ord(letter)<=ord("Z"):
            letters+=1
        #elif ord("!")<=ord(letter)<=ord("@") or ord("[")<=ord(letter)<=96 or 123<=ord(letter)<=126:
        elif letter in punctuation:
            marks+=1
    text=f"Line {my_list_row+1}: {my_list[my_list_row][0:-1]} ({letters})({marks})\n"
    my_output.write(text)
my_output.close()
my_file.close()

