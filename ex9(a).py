
infile =open("/Users/divakarv/diva/file.dat","r")
outfile =open("/Users/divakarv/diva/file1.dat","w")

sum=0
s=infile.read()
numbers=[int(x) for x in  s.split()]
print("The numbers are")
print(numbers)
for num in numbers:
    sum=sum+num
sum=str(sum)
outfile.write("Sum is")
outfile.write(sum)
print(sum)

infile.close()
outfile.close()
