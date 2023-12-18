def strlen(str):
    count=0
    while str[count:]:
        count+=1
    return count

def  strrev(str):
    l=strlen(str)
    rstr=""
    while(l>0):
       rstr=rstr+str[l-1]
       l=l-1
    return rstr


def strcon(st1,st2):
    return (st1+st2)

def strcom(st1,st2):
    if(st1==st2):
        print(str1," and", str2," are equal")
    else:
        print("String 1 and string 2 are not equal")

print("1.string length \n2.string reverse \n3.string concatenation \n4.string comparison")
n=int(input("Enter your choice : "))
if n==1:
    str=input("Enter string :")
    print("Length of the string ",strlen(str))

elif n==2:
    str=input("Enter string :")
    print("Reversed string is ",strrev(str))

elif n==3:
    str1=input("Enter string 1 :")
    str2=input("Enter string 2 :")
    print("Concadenated string is ",strcon(str1,str2))

elif n==4:
     str1=input("Enter string 1 :")
     str2=input("Enter string 2 :")
     strcom(str1,str2)

else:
    print("Enter  valid choice")
 
