employeeData=[
    {'name':'RAM', 'salary': 35000, 'bonus':2},
    {'name':'SAM', 'salary': 65000, 'bonus':5},
]

class Employee:
    
    def __init__(self,name,salary,bonus):
        self.name=name
        self.salary=salary
        self.bonus=bonus
        self.bonusAmt=self.salary*(self.bonus/100)
        pass

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary}, bonus={self.bonus}%)"
    def bonusCal(self):
        bonusAmt=self.salary*(self.bonus/100)
        pass
    def salaryStructure(self):
        return f"Employee's Name = {self.name}\nSalary = Rs. {self.salary}\nBonus %age = {self.bonus}%\nBonus Amount = Rs. {self.bonusAmt}\nTotal Salary(Salary + Bonus) = Rs. {self.salary+self.bonusAmt}"
    


for employee in employeeData:
    globals()[employee['name']] = Employee(employee['name'],employee['salary'],employee['bonus'])
    pass
for employee in employeeData:
    print(globals()[employee['name']].salaryStructure())
