try:
    num1,num2=eval(input("Enter number 1 ad number 2 separated by comma : "))
    result=num1/num2
    print("Result is ",result)
    if(num1==0):
      raise RuntimeError()
except ZeroDivisionError:  
     print("Division by Zero !")

except SyntaxError:
         print("May be comma is mising !")

except RuntimeError:
         print("may be meaning less !")

except:
         print("Something went wrong in the input !")

else:
     print("No Exceptions !")

finally:
    print("Finally vlause is executed !")
