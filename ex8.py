class distance:
    def __init__(self,f,i):
        self.feet=f
        self.inches=i
    def __gt__(self,d2):
        if(self.feet>d2.feet):
            return (True)
        if((self.feet==d2.feet)and(self.inches>d2.inches)):
            return (True)
        else:
            return (False)
    def __add__(self,d2):
        f=self.feet+d2.feet
        i=self.inches+d2.inches
        if(i>=12):
            i=i-12
            f=f+1
        return distance(f,i)
    def show(self):
        print("Distance 3 feet is ",self.feet,"inches is",self.inches)


 

    
p1=distance(8,4)
p2=distance(6,9)
p3=p1+p2
p3.show()
if(p1>p2):
    print("p1 is geater than p2")
else:
    print("p1 is less than or equal to p2")
