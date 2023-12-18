import math

class point:
    def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c
    def distancefromorgin(self):
        ans=((self.x**2)+(self.y**2)+(self.z**2))**0.5
        return ans
    def distance(self,p2):
        xdiff=self.x-p2.x
        ydiff=self.y-p2.y
        zdiff=self.z-p2.z
        ans=math.sqrt((xdiff**2)+(ydiff**2)+(zdiff**2))
        return ans


a,b,c=(input("Enter point 1 coefficient of x,y,z:")).split()
d,e,f=(input("Enter point 2 coefficient of x,y,z :")).split()
a,b,c=[int(a),int(b),int(c)]
d,e,f=[int(d),int(e),int(f)]
p1=point(a,b,c)
p2=point(d,e,f)

print("the distancle from point 1 and orgin is ",p1.distancefromorgin())
print("the distancle from point 2 and orgin is ",p2.distancefromorgin())
print("the distance between point  1 and point 2 is ",p1.distance(p2))
