# BASICS OF OOPS and __init__

class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram


    def config(self):
        print('config is :',self.cpu,self.ram)


com1=computer('i5',16)
com2=computer('Ryzen 3',8)

com1.config()
com2.config()




#Constructor and self

class computer:
    def __init__(self):
        self.name='Naveen'
        self.age=28

    def update(self):
        self.age=20

    def compare(self,c1):
        if self.age==c1.age:
            return True
        else:
            return False


c1=computer()
c1.age= 12

c2=computer()


if c2.compare(c1):
    print('They are same')
else:
    print('They are Different')


print(c1.name)
print(c1.age)

print(c2.name)
print(c2.age)




#Types of variables

class car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.com='BMW'

c1=car()
c2=car()
car.wheels=5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)




#Types of Methods

class student:
    school="Sacred Heart"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):#instance method
        return (self.m1+self.m2+self.m3)/3


    @classmethod   
    def getSchoolName(cls):#class method
        return cls.school
    
    @staticmethod
    def info():#static method
        print('This is Student class')


s1=student(34,53,54)
s2=student(45,67,82)
print(s2.avg())

print(student.getSchoolName())
student.info()






#Class inside a class

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap. show()

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student('Pradeen',18)
s2=student('Vasu',24)
s1.show()

lap1=student.Laptop()
lap2=student.Laptop()


#inheritance

class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('Feature 1-A working')

    def feature2(self):
        print('Feature 2 working')

class B:
    def __init__(self):
        print('in B init')

    def feature1(self):
        print('Feature 1-B working')

    def feature4(self):
        print('Feature 4 working')

class C(B,A):
    def __init__(self):
        super().__init__()
        print('in C init')

    def feature3(self):
        print('Feature 3 working')

    def feat(self):
        super().feature4()


a1=C()
a1.feat()


#Polymorphism


#Ducktyping

class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('spell check')
        print('convention check')
        print('compiling')
        print('Running')

class Laptop:
    def code(self,ide):
        ide.execute()

ide=MyEditor()

lap1=Laptop()
lap1.code(ide)

print(type(ide))



#operator overloading

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3  
    def __gt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1>s2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
        
    

    
s1=student(24,53)
s2=student(13,54)
s3=s1+s2

if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')

print(s1)
print(s2)



#Method overloading

class student:
    def __init__(self,m1,m2) :
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        if a and b and c:
            s=a+b+c
        elif a and b:
            s=a+b
        elif a:
            s=a
        else:
            return None
        return s 
s1=student(45,33)
print(s1.sum(4,5,6))


#Method overriding

class A:
    def show(self):
        print('in A show')

class B(A):
    def show(self):
        print('in B show')

a1=B()
a1.show()

