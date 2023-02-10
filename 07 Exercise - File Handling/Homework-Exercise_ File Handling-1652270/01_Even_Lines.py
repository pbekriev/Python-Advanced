with open("text1.txt") as my_file:
    my_list=my_file.readlines()
for i in range(0,len(my_list),2):
    my_list[i]="".join(map(lambda x: "@" if x in ["-", ",", ".", "!", "?"] else x,my_list[i]))
    [print(my_list[i].split()[y],end=" ") for y in range(len(my_list[i].split())-1,-1,-1)]
    print()
