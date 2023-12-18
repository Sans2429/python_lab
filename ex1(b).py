lower=int(input("Enter  the lower limit :"))
upper=int(input("Enter  the upper limit :"))


print("Prime numbers between ",lower,"and",upper)
num=lower
while(num<=upper):
    
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
    num+=1
     
     
