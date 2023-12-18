import math,cmath

a,b,c=(input("Enter coefficient of  a,b,c :")).split()
a,b,c=[int(a),int(b),int(c)]
d=(b**2)-(4*a*c)
if d==0:
    sol1=-b/(2*a)
    sol2=-b/(2*a)
    print("Roots are real and equal")
if d>0:
    sol1=(-b-(math.sqrt(d)))/(2*a)
    sol2=(-b+(math.sqrt(d)))/(2*a)
    print("Roots are real and unequal")
if d<0:
    sol1=(-b-(cmath.sqrt(d)))/(2*a)
    sol2=(-b+(cmath.sqrt(d)))/(2*a)
    print("Roots are real and imaginary")

print("{0} and {1}".format(sol1,sol2))
          

