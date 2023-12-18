class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

class employee(person):
    def __init__(self,n,a,d,s):
        person .__init__(self,n,a)
        self.dist=d
        self.salary=s
    def show(self):
        print("Student details :\nName :",self.name,"\nAge :",self.age,"\ndistinaition :",self.dist,"\nSalary :",self.salary)
class student:
    def __init__(self,rno):
        self.rno=rno
class resident(person,student):
    def __init__(self,n,a,rno):
        person .__init__(self,n,a)
        student .__init__(self,rno)

    def show(self):
        print("Resident details :\nName :",self.name,"\nAge :",self.age,"\nroom no",self.rno)

e1=employee("Diva",19,"student","-")
e2=resident("kathi",45,7890)
e1.show()
e2.show()
            
    
