class Employee:
    def __init__(self):
        self.emp=[]
        
    def addEmployee(self):
        print('\nEnter Employee Name')
        count=int(input('how many employee you would like to a add:'))
        for i in range(count):
            ename=input()
            self.emp.append(ename)

    def viewEmployee(self):
        print('\n List of Employees')
        for sno,name in enumerate(self.emp,1):
            print(sno,'\t',name)

    def removeEmployee(self):
        name=input('Enter the name you would like to delete:')
        if name in self.emp:
            self.emp.remove(name)
            print('Employee deleted')
        else:
            print('invalid name')

obj=Employee()

while True:
    print('\n')
    print('1.Add Employee')
    print('2.View Employee')
    print('3.Delete Employee')
    print('4.Exit')
    
    data=int(input('Please Enter your Operation:'))
    if data==1:
        obj.addEmployee()
    elif data==2:
        obj.viewEmployee()
    elif data==3:
        obj.removeEmployee()
    else:
        quit()