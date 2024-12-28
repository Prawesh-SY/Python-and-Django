# WAP to make a system for computer shop to store computers like, computer name, brand, Price, ID, generation, core
from datetime import datetime
from prettytable import PrettyTable

current_time = datetime.now()

class ComputerShop:
    
    def __init__(self,file_path):
        self.fileList=[]
        self.file_path=file_path
        self.fileList.append(self.file_path)
             
    def menu(self,storeName):
        displayMessage=f"""
            !!! {storeName} !!!
        Please select an option:
        
        1. Add inventory
        2. Check inventory
        3. Transaction
        4. Delete from inventory
        5. Exit
            
        """
        print(displayMessage)
        
    def displayAllfiles(self):  # Not in use currently # This function will return the names of all file created by the user
        for file in self.fileList:
            print(f"File Name: {file}")
        pass
    def checkInExsistingFile(self,checkForFile):   # Not in use currently # This function will return True if the file exsists in the fileList 
        for file in self.fileList:
            if checkForFile in file:
                return True
        pass
    
    def add(self,allData):  # Add Inventory
        for item in allData:
            with open(self.file_path,'a+') as fileObj:
                fileObj.write(item)
                fileObj.close()
        self.read()
            
    def read(self):
        table = PrettyTable()
        table.field_names = ["DATE","STAFF NAME","BRAND","MODEL NO.","RATE","CORE","ID","QUANTITY"," "]
        print("""
                                                    !!! INVENTORY !!!
              """)
        with open(self.file_path,'r') as fileObj:
            data = fileObj.readlines()
            fileObj.close()
            for line in data:
                fields = line.split(",")
                table.add_row(fields)
            print(table)
                
                # if len(temp) >=9:
                #     for i in range(len(temp)-1):
                #         print(temp[i],end="|")
                #     print("\n")
                    # print("Staff:",temp[1])
                    # print("Brand: ",temp[2])
                    # print("Model no.: ",temp[3])
                    # print("Rate: ",temp[4])
                    # print("Core: ",temp[5])
                    # print("ID: ",temp[6])
                    # print("Quantity: ",temp[7])
                    # print(temp[8])
                # else:
                #     print("Incomplete Log: ",temp,"\n")
                
            
    def delete(self,toBeDeleted):
        requiredLog = self.logSearch(toBeDeleted)
        # print(requiredLog)
        if requiredLog is not None:
            with open(self.file_path, 'r') as file:
                data = file.readlines()
                # print(data)
                data.remove(requiredLog)
                file.close()
            with open(self.file_path,'w+') as file:
                for log in data:
                    file.write(log)
                file.close()
            
        
    def trx(self):
        updateConsole="""
            !!! UPDATE !!!
        Please select an option:
        1. Sales (Goods sold from the Inventory)
        2. Sales Return (Goods to be added in the Inventory)
        """
        print(updateConsole)
        option = input('User Input: ')
        if option == '2':   # Sales Return
            self.read()
            id = input("Enter the ID of the product to be returned: ")
            qty = input("Enter the quantity of the product to be returned: ")
            self.salesReturn(id,qty)
            self.read()
        elif option == '1': # Sales
            self.read()
            id = input("Enter the ID of the product to be purchased: ")
            qty = input("Enter the quantity of the product to be purchased: ")
            self.sales(id,qty)
            self.read()
            pass
        else:
            print("Invalid input")
            
    def sales(self,id,qty):
        requiredLog = self.logSearch(id)
        if requiredLog != None:
            requiredLog = requiredLog.split(",")
            if int(requiredLog[-2]) >= int(qty) :
                requiredLog[-2]=int(requiredLog[-2])-int(qty)
            elif int(requiredLog[-2]) < qty:
                print("The number product is not sufficient to complete the sales")
            elif int(requiredLog[-2]) == 0:
                print("The product is not available right now")
            # print(requiredLog)
            self.trxComplete(requiredLog,id)
        else:
            pass
    
    def salesReturn(self,id,qty):
        requiredLog = self.logSearch(id)
        requiredLog = requiredLog.split(",")
        requiredLog[-2]=int(requiredLog[-2])+int(qty)
        self.trxComplete(requiredLog,id)
        
    def trxComplete(self,requiredLog,id):
        with open(self.file_path, 'r+') as file:
            data = file.readlines()
            file.close()
        # print(data)
        temp=None
        for item in data:
            # print(item)
            if id in item:
                temp = item
                data.remove(temp)
                # print(temp)
        # print(data)
        if temp ==None:
            print(f"The log with ID {id} not found")
        trxComplete=''
        for x in requiredLog:
            if x !="\n":
                trxComplete = trxComplete+str(x)+","
            else:
                trxComplete=trxComplete+str(x)
        data.append(trxComplete)
        with open(self.file_path, "w+") as file:
            for item in data:
                file.write(item)
            file.close()
            
    def logSearch(self,searchKey):
        with open(self.file_path, 'r+') as file:
            data = file.readlines()
            file.close()
        # print(data)
        requiredLog=None
        for item in data:
            # print(item)
            if searchKey in item:
                requiredLog = item
                # data.remove(requiredLog)
                # print(requiredLog)
        if requiredLog ==None:
            print(f"The log with ID {searchKey} not found")
        return requiredLog

        
EvoStore = ComputerShop("EvoStoreInventory.txt")
while True:
    EvoStore.menu("Evo Store")
    option = input("User Input: ")
    if option == '1':   # Create inventory
        date =  str(datetime.now())
        staffName =  input("Enter your name: ")
        computerBrand = input("Enter the Computer Brand: ")
        modelNumber = input("Model No.: ")
        price = input("Price: ")
        id = input("ID: ")
        cpu=  input("Core Used: ")
        quantity =  input("Quantity: ")
        allData=[]
        allData.extend([date,",",staffName,",",computerBrand,",",modelNumber,",",price,",",cpu,",",id,",",quantity,",",'\n'])
        EvoStore.add(allData)
        
    elif option == '2':     # Check inventory
        EvoStore.read()
           
    elif option == "3":     # Update inventory
        EvoStore.trx()
                  
    elif option == "4":     # Delete from inventory
        EvoStore.read()
        toBeDeleted=input("Enter the log to be deleted: ")
        EvoStore.delete(toBeDeleted)
        EvoStore.read()
            
        # else:
        #     print(f"The file '{fileName}' not found")
        pass
    elif option == "5":     # Exit
        exit()
    
    else:
        print("!!Invalid User Input!!")