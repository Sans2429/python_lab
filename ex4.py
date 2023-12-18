def lar(lst):
    l=lst[0]
    for i in range(1,n):
        if(l<lst[i]):
            l=lst[i]
    return l
lst=[]
n=int(input("Enter total no of elements in the list :"))
for i in range(n):
    a=int(input())
    lst.append(a)
print("The elements in list are",lst)
print("The largest element in the list is ",lar(lst))
