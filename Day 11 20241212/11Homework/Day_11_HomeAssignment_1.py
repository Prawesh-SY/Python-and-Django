# Make a student information Management System

class SIMS:
    def navigation(self, option: int)->str:
        nav=SIMS
        if option==1:
            nav.enquire
    def homePage()-> int:
        sol=SIMS()
        welcomeMessage="""
        Welcome to Student Information Management System
        Please select one of  the option below:
            1. New Enquiry
            2. New Admission
            3. Search Student's Information
            4. Update Student's Information
            5. Exit
"""
        print(welcomeMessage)
        sol.navigation(option=input("User Input: "))


    def login():
        print("This page is under construction")
    def enquire():
        print("This page is under construction")
    def createNewAdmission():
        print("This page is under construction")
    def readStudent():
        print("This page is under construction")
       
    def updateStudent():
        print("This page is under construction")
    
    def delete():
        print("This page is under construction")

run=SIMS()
welcomeMessage="""
                SKILLSHIKSHYA 
        Welcome to Student Information Management System
        Please select one of  the option below:
            1. New Enquiry
            2. New Admission
            3. Search Student's Information
            4. Delete Student Information(Function Under Construction)
            5. Exam Seciton
            6. Exit
"""

enquires=[{ 'name':'Ram','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Shyam','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Hari','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Sagar Giri','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Kiran','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Sandesh Bhusal','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Pukar Bade','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Ujjwal','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Sushil Shrestha','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Pukar Bade','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Promish','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Sailendra','number':'9865122175','class':'10','message':"All iz Well!",},
          { 'name':'Sushil Bohara','number':'9865122175','class':'10','message':"All iz Well!",},
        ]
students=[{"name":'Prawesh','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':'',},
          {"name":'Prawesh','class':'10','section':'B','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':'',
           "UT-1":{'ENGLISH':30,'NEPALI':45},
           "MID-TERM": {'ENGLISH': 100,'NEPALI':99,'MATHS':100,'SCIENCE':100,'SOCIAL STUDIES':100},
           "UT-2":{'ENGLISH':30,'NEPALI':45}
           },
          {"name":'Pratima Dhakal','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
          {"name":'Bigendra Shrestha','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
          {"name":'Priyanka','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
          {"name":'Pashupati','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
          {"name":'Alisha Sharma','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
          {"name":'Manoj Kumar Das','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
          {"name":'Ashok Thapa','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
          {"name":'Shrish Pokhrel','class':'10','section':'A','dob':'','fatherName':'','fatherMobile':'','motherName':"",'motherMobile':''},
        ]
homepageCommand='y'
while homepageCommand=='y':
    print(welcomeMessage)
    userInput = input("User Input: ")
    if userInput=="1":     #New Enquiry     #Completed
        enquireCommand='y'
        while enquireCommand=='y':
            enquire={
                'name':'',
                'number':'',
                'class':'',
                'message':"",        
            }
            enquire["name"]=input("Your name: ")
            enquire["number"]=input('Your contact number: ')
            enquire["class"]=input("Your ward is in garde: ")
            enquire["message"]=input('Message\n')
            enquires.append(enquire)
            print(enquire)
            enquireCommand=input("Do you wish to make another enquire(y/n): ")
            if enquireCommand == 'n':
                homepage=input('Do you wish to return to Home(y/n): ')
            elif enquireCommand == 'y':
                print("Next query\n")
    elif userInput=='2':    #New Admission  #Completed
        newAdmissionCommnd='y'
        while newAdmissionCommnd=='y':
            student={
                "name":'',
                'class':"",
                'section':'',
                'dob':'',
                'fatherName':'',
                'fatherMobile':'',
                'motherName':"",
                'motherMobile':''

            }
            displayMessage="""
            !!!NEW ADMISSION!!!
"""
            print(displayMessage)
            student['name']=input("Student's Name:")
            student['class']=input("Class: ")
            student['section']=input("Section: ")
            student['dob']=input(f"Date of Birth of {student['name']}:\n")
            student['fatherName']=input(f"Father's Name:\n")
            student['fatherMobile']=input("Father's Mobile No.:\n")
            student['motherName']=input("Mother's Name:\n")
            student['motherMobile']=input("Mother's Mobile No.:\n")
            students.append(student)
            print(student)
            newAdmissionCommnd=input("Next student (y/n): ")
    elif userInput=='3':    # Search Student's Info     #COMPLETED
        searchCommand='y'
        while searchCommand=='y':
            displayMessage="""
                SEARCH STUDENT'S INFORMATION
            Please select one of the option given below:
            1. Search Enquire
            2. Search Student
            3. Exit Search

    """
            print(displayMessage)
            searchInput=input("User Input: ")
            if searchInput=='1':       # Search Enquire       COMPLETED
                if enquires != []:
                    enquireSearchKey=input("Search: ")
                    searchStatusBar="|"
                    searchResult=[]
                    for i in enquires:  # Here 'i' contains the dictionaries in the list 'enquires'
                        # print(i)
                        print ("|",end=searchStatusBar)
                        for key in i:       # Here 'key' contains the keys of the dictionary "i"
                            print ("|",end=searchStatusBar)
                            # print(key)
                            # print(i[key])     # Here 'i[key]' contains the values of dictionary "i"
                            if enquireSearchKey in i[key]:
                                searchResult.append(i)
                                searchStatusBar=searchStatusBar+"|"
                            if enquireSearchKey in key:
                                searchResult.append(i)
                                searchStatusBar=searchStatusBar+"|"
                            else:
                                searchStatusBar=searchStatusBar+"|"
                                # searchCommand=input("Do you wish to search again(y/n): ")
                    if searchResult==[]:        #   COMPLETED
                        print("\nNo data found\n")
                    else:       # COMPLETED
                        print("\n")
                        print(searchResult)
                        print("\n") 
                    searchCommand=input("Do you wish to search again(y/n): ")
                else:       #COMPLETED
                    print("Sorry, no Enquires has been made yet")
                    searchCommand=input("Do you wish to search again(y/n):") 
                
            elif searchInput=='2':      # Search Student    COMPLETED
                if students != []:
                    studentSearchKey=input("Search: ")
                    searchStatusBar="|"
                    searchResult=[]
                    for i in students:  # Here 'i' contains the dictionaries in the list 'students'
                        # print(i)
                        print ("|",end=searchStatusBar)
                        for key in i:       # Here 'key' contains the keys of the dictionary "i"
                            print ("|",end=searchStatusBar)
                            # print(key)
                            # print(i[key])     # Here 'i[key]' contains the values of dictionary "i"
                            if studentSearchKey in i[key]:
                                searchResult.append(i)
                                searchStatusBar=searchStatusBar+"|"
                            if studentSearchKey in key:
                                searchResult.append(i)
                                searchStatusBar=searchStatusBar+"|"
                            else:
                                searchStatusBar=searchStatusBar+"|"
                                # searchCommand=input("Do you wish to search again(y/n): ")
                    if searchResult==[]:        #   COMPLETED
                        print("\nNo data found\n")
                    else:       # COMPLETED
                        print("\n")
                        print(searchResult)
                        print("\n")
                    searchCommand=input("Do you wish to search again(y/n): ")
                else:       #COMPLETED
                    print("Sorry, no Admission has been made yet")
                    searchCommand=input("Do you wish to search again(y/n):") 
            elif searchInput=="3":  # Exit Search    # COMPLETED
                break
            else:                   #INVALID INPUT   # COMPLETED
                print("INVALID INPUT!\n")
                searchCommand=input("Do you wish to search again(y/n): ")
    elif userInput == '4':  # Delete Student Info #PENDING
        
        pass
    elif userInput=='5':    #Exam Section   #Pending
        updateCommand="y"
        while updateCommand=='y'or"Y":  # COMPLETED
              displayMessage="""
                        EXAM SECTION
            Please select one of the option given below:
            1. Student's Exmination Marks Entry
            2. Change/Update Student's Examination Marks
            3. Search Student's Report Card
            4. Delete Student's Examination Marks
            5. Go to Home Page

    """
              print(displayMessage)
              updateInput=input("User Input: ")
              if updateInput=='1':      #  Student's Exmination Marks Entry
                  examCommand='y'
                  while examCommand=='y':
                      studentName=input("Enter Student's Name: ")
                      studentClass=input("Enter Student's Class: ")
                      studentSection=input("Enter Student's Section: ")
                      for i in students:
                          if studentName in i.values():
                              if studentClass in i.values():
                                  if studentSection in i.values():
                                      print(i)
                                      exam=input("Enter Exam Type(UT-1/MID-TERM/UT-2/TERM): ")
                                      keys=[]
                                      values=[]
                                      for  n in range(7):
                                        keys.append(input("Enter Subject[ALL CAPS]: "))
                                        values.append(float(input("Enter marks obtained: ")))
                                        pass
                                      examMarks=dict(zip(keys,values))
                                      i.setdefault(exam,examMarks)
                                      print(i)
                      examCommand=input("Add  next Student's Examination Marks(y/n): ")                          
              elif updateInput=='2':    # Change/Update Student's Examination Marks
                examCommand='y'
                while examCommand=='y':
                    studentName=input("Enter Student's Name: ")
                    studentClass=input("Enter Student's Class: ")
                    studentSection=input("Enter Student's Section: ")
                    examType=input("Exam Type (UT-1/MID-TERM/UT-2/TERM): ")
                    foundStudentName=False
                    foundStudentClass=False
                    foundStudentSection = False
                    foundExamType = False
                    examMarks={}
                    for i in students:                        
                          #   print(i)
                          if studentName in i.values(): #COMPLETED
                            foundStudentName=True
                            if studentClass in i.values():
                                  foundStudentClass=True
                                  if studentSection in i.values():
                                      foundStudentSection = True
                                      if examType in i.keys():
                                          foundExamType = True
                                          keys=[]
                                          values=[]
                                          for  n in range(7):
                                            keys.append(input("Enter Subject[ALL CAPS]: "))
                                            values.append(float(input("Enter marks changed/updated: ")))
                                          examMarks=dict(zip(keys,values))
                                          i[examType].update(examMarks)
                                          print(i)
                    if examMarks == {}:
                      if foundStudentName == False:     #COMPLETED
                          print(f"{studentName} is not registered as a student")
                          pass
                      elif foundStudentClass == False:  #COMPLETED
                          print(f"{studentName} is not registered in class {studentClass}")
                          pass
                      elif foundStudentSection == False:    #COMPLETED
                          print(f"No student named {studentName} is registered in Class: {studentClass}'{studentSection}'")
                          pass
                      elif foundExamType == False:
                          print(f"The marks of {examType} has not been registered for {studentName} yet")
                          pass
                      pass
                    examCommand=input("Change/Update next Student's Examination Marks(y/n): ")
              elif updateInput=='3':    # Search Student's Report Card  #COMPLETED
                   examCommand='y'
                   while examCommand=='y':
                        searchResult=[]
                        studentName=input("Enter Student's Name: ")
                        studentClass=input("Enter Student's Class: ")
                        studentSection=input("Enter Student's Section: ")
                        foundStudentName=False
                        foundStudentClass=False
                        foundStudentSection = False
                        foundExamType = False
                        for i in students:                            
                            if studentName in i.values():
                                foundStudentName=True
                                if studentClass in i.values():
                                    foundStudentClass = True
                                    if studentSection in i.values():
                                        foundStudentSection= True
                                        for key,value in i.items():
                                            searchResult.append({key,value})
                                            print(f"{key} : {value}")
                                            pass
                                        pass
                                    pass
                                pass
                            pass
                        if searchResult==[]:
                            if foundStudentName == False:
                                print(f"{studentName} is not registered as a student")
                                pass
                            elif foundStudentClass == False:
                                print(f"{studentName} is not registered in class {studentClass}")
                                pass
                            elif foundStudentSection == False:
                                print(f"No student named {studentName} in registered in {studentClass}{studentSection}")
                                pass
                            elif foundExamType == False:
                                print(f"The marks of {examType} has not been registered for {studentName} yet")
                                pass
                            pass
                        examCommand=input("Search for Next Student's Report Card(y/n): ")
              elif updateInput=='4':    # Delete Student's Examination Marks
                  examCommand='y'
                  while examCommand=='y':
                    deleteDisplayMessage=f"""
                        !!! CONFIRM DELETION !!!
                        Please select an option below:
                        1. Delete the Student's Examination Marks from the Database
                        2. Go to EXAM SECTION
"""
                    print(deleteDisplayMessage)
                    deletcommand=input("User Input: ")
                    if deletcommand == '1':     # Delete Student's Exam marks from Database
                        studentName=input("Enter Student's Name: ")
                        studentClass=input("Enter Student's Class: ")
                        studentSection=input("Enter Student's Section: ")
                        searchResult=[]
                        foundStudentName=False
                        foundStudentClass=False
                        foundStudentSection = False
                        foundExamType = False
                        for i in students:
                            #   print(i)
                            if studentName in i.values():
                                foundStudentName=True
                                if studentClass in i.values():
                                    foundStudentClass=True
                                    if studentSection in i.values():
                                        foundStudentSection=True
                                        for key,value in i.items():
                                            # searchResult.append({key,value})
                                            print(f"{key} : {value}")
                                            pass
                                        deleteOptionMessage="""
                !!! DELETE RESULT !!!
                1. Delete UT-1 RESULT
                2. Delete MID-TERM RESULT
                3. Delete UT-2 RESULT
                4. Delete TERM RESULT
                5. Cancel Deletion
"""
                                        deleteResultCommand='y'
                                        while deleteResultCommand == "y":
                                            print(deleteOptionMessage)
                                            confirmDelete=input("User Input: ")
                                            if confirmDelete == '1':    # Delete UT-1 RESULT
                                                if "UT-1" in i.keys():
                                                    examType=True
                                                    del i["UT-1"]
                                                    print("Exam Results Deleted")
                                                    print(i)
                                                    pass
                                                else:
                                                    print("NO result found")
                                                    break
                                                pass
                                            elif confirmDelete == '2':  # Delete MID-TERM RESULT
                                                if "MID-TERM" in i.keys():
                                                    examType=True
                                                    val=i.pop("MID-TERM")
                                                    print("Exam Results Deleted")
                                                    print(i)
                                                    pass
                                                else:
                                                    print("NO result found")
                                                    break
                                                pass
                                            elif confirmDelete == '3': # Delete UT-2 RESULT
                                                if "UT-2" in i.keys():
                                                    examType=True
                                                    val=i.pop("UT-2")
                                                    print("Exam Results Deleted")
                                                    print(i)
                                                    pass
                                                else:
                                                    print("NO result found")
                                                    break
                                                pass
                                            elif confirmDelete=='4':    # Delete TERM RESULT
                                                if "TERM" in i.keys():               
                                                    examType=True
                                                    del i["TERM"]
                                                    print("Exam Results Deleted")
                                                    print(i)
                                                    pass
                                                else:
                                                    print("NO result found")
                                                    break
                                            elif confirmDelete == '5':  # Cancel Deletion #TESTING
                                                print("Deletion Cancelled!")
                                                break
                                            else:                       # Invalid user input # COMPLETED
                                                print("INVALID INPUT\n")
                                                deleteResultCommand = input("Do you wish to stay on DELETE RESULT page(y/n): ")
                                                if deleteResultCommand == 'y':  # Back to DELETE RESULT #COMPLETED
                                                    continue
                                                else:                           # Back to CONFIRM DELETION #COMPLETED
                                                    break
                        if searchResult==[]:
                            if foundStudentName == False:
                                print(f"{studentName} is not registered as a student")
                                pass
                            elif foundStudentClass == False:
                                print(f"{studentName} is not registered in class {studentClass}")
                                pass
                            elif foundStudentSection == False:
                                print(f"No student named {studentName} in registered in {studentClass}{studentSection}")
                                pass
                            elif foundExamType == False:
                                if confirmDelete == '1':    # UT-1
                                    examName="UT-1"
                                elif confirmDelete =='2':   # MID-TERM
                                    examName="MID-TERM"
                                elif confirmDelete == '3':  # UT-2
                                    examName="UT-2"
                                elif confirmDelete== '4':   # TERM
                                    examName="TERM"
                                print(f"The marks of {examName} has not been registered for {studentName} yet")
                                pass
                            pass                            
                    elif deletcommand == '2':   # Go to STUDENT'S EXAMINATION INFORMATION   # COMPLETED
                        break
                    else:                       # COMPLETED
                        print("INVALID INPUT\n")    
                        stayOnConfirmDeletion=input("Do you wish to stay on the 'CONFIRM DELETION' page(y/n): ")
                        if stayOnConfirmDeletion == 'y':
                            continue
                        else:
                            break
                    
                    examCommand=input("Delete next Student's Examination Marks(y/n): ")
                  pass
              elif updateInput=='5':    # Go to Home Page #Completed
                  break
              else:                     # Invalid Input message # COMPLETED
                  print("INVALID INPUT\n")
                  updateCommand=input("Do you wish to stay on the STUDENT'S EXAMINATION INFORMTION (y/n): ")
    elif userInput=='6':    #Exit   #Completed
        exit()
                

    


