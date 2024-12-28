mod = ['w', 'r', 'w+', 'r+', 'a', 'wb', 'rb']

# with open("fileName.extentions", "mode") as variable:
    # pass
    
with open("readme.txt",'w') as file_obj:
    file_obj.write("Hello World!\nHello Python!\nHello Prawesh!")
    
with open("readme.txt","r+") as file_obj:
    allData = file_obj.read()
    oneLine = file_obj.readline()
    allLines = file_obj.readlines()
    file_obj.write("\nHello Class!!")
    
print(allData,"\n")
print(oneLine,"\n")
print(allLines,"\n")