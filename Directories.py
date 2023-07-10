from pathlib import Path

path = Path(".vscode")
print(path.exists())   #check if dir exists
print(path.mkdir())    #make directories
print(path.rmdir())    #remove directory

print("================================================")

path_1 = Path()            #no argument means python directory
for file in path_1.glob("*.*"):    #*.* gets all files, * gets everything,  *.py gets python files, *.xlsx gets excel sheets etc
    print(file)         