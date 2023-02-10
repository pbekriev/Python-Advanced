import os

while True:
    commands =input().split("-")
    if commands[0]=="End":
        break
    if commands[0]=="Create":
        my_file=open(commands[1],"w")
        my_file.close()
    if commands[0]=="Add":
        my_file = open(commands[1], "a")
        my_file.write(commands[2]+"\n")
        my_file.close()
    if commands[0]=="Replace":
        try:
            my_file = open(commands[1], "r")
            my_list=my_file.readlines()
            old_str,new_str=commands[2],commands[3]
            for row in range(len(my_list)):
                my_list[row]=my_list[row].replace(old_str,new_str)
            my_file.close()
            my_file=open(commands[1],"w")
            my_file.writelines(my_list)
            my_file.close()
        except FileNotFoundError:
            print("An error occurred")
    if commands[0]=="Delete":
        try:
            os.remove(commands[1])
        except FileNotFoundError:
            print("An error occurred")
