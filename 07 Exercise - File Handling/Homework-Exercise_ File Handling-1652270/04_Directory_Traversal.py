import os
dict_dir={}
list_dir =os.listdir()
for list_dir_row in list_dir:
    index_dot_start=-1
    while True:
        index_dot=list_dir_row.find(".",index_dot_start+1)
        if index_dot==-1:
            break
        else:
            index_dot_start=index_dot
    if index_dot_start!=-1:
        extension=list_dir_row[index_dot_start:]
        if extension not in dict_dir:
            dict_dir[extension]=[]
        dict_dir[extension].append("- - - "+list_dir_row+"\n")
dict_dir=sorted(dict_dir.items(), key=lambda x: (x[0],x[1]))
my_report=open("report.txt", "w")
for dict_dir_row in dict_dir:
    my_report.write(dict_dir_row[0]+"\n")
    my_report.writelines(dict_dir_row[1])
